"""
Wolkenkraft Mini Vape Inlay STL Generator

Estimated dimensions based on photos:
- Outer body ~30mm wide, ~18mm deep, ~68mm tall (inlay portion only)
- Wall thickness 2.5mm
- Buttons on narrow front face
- USB-C cutout at bottom center
- Open top and bottom
"""

import numpy as np
from stl import mesh

def rounded_rect_polygon(w, d, r, n=12):
    """2D rounded rectangle vertices (CCW), centered at origin."""
    pts = []
    corners = [
        ( w/2 - r,  d/2 - r, 0),
        (-w/2 + r,  d/2 - r, np.pi/2),
        (-w/2 + r, -d/2 + r, np.pi),
        ( w/2 - r, -d/2 + r, 3*np.pi/2),
    ]
    for cx, cy, start in corners:
        for i in range(n):
            a = start + i * (np.pi/2) / n
            pts.append((cx + r*np.cos(a), cy + r*np.sin(a)))
    return np.array(pts)

def extrude_polygon(poly2d, z0, z1):
    """Extrude a closed 2D polygon into triangles (side walls + caps)."""
    tris = []
    n = len(poly2d)
    # Side walls
    for i in range(n):
        j = (i + 1) % n
        p0 = (*poly2d[i], z0)
        p1 = (*poly2d[j], z0)
        p2 = (*poly2d[i], z1)
        p3 = (*poly2d[j], z1)
        tris.append([p0, p1, p2])
        tris.append([p1, p3, p2])
    # Caps (fan triangulation from centroid)
    c = poly2d.mean(axis=0)
    for i in range(n):
        j = (i + 1) % n
        # Bottom cap (normal down)
        tris.append([(*c, z0), (*poly2d[j], z0), (*poly2d[i], z0)])
        # Top cap (normal up)
        tris.append([(*c, z1), (*poly2d[i], z1), (*poly2d[j], z1)])
    return tris

def hollow_prism(outer_w, outer_d, inner_w, inner_d, r_out, r_in, z0, z1, n=16):
    """Hollow rounded rect prism, open top and bottom (walls only)."""
    outer = rounded_rect_polygon(outer_w, outer_d, r_out, n)
    inner = rounded_rect_polygon(inner_w, inner_d, r_in, n)
    tris = []
    m = len(outer)  # == len(inner)
    for i in range(m):
        j = (i + 1) % m
        o0 = (*outer[i], z0); o1 = (*outer[j], z0)
        o2 = (*outer[i], z1); o3 = (*outer[j], z1)
        i0 = (*inner[i], z0); i1 = (*inner[j], z0)
        i2 = (*inner[i], z1); i3 = (*inner[j], z1)
        # Outer wall
        tris += [[o0, o1, o2], [o1, o3, o2]]
        # Inner wall (reversed)
        tris += [[i0, i2, i1], [i1, i2, i3]]
        # Bottom ring
        tris += [[o0, i0, o1], [o1, i0, i1]]
        # Top ring
        tris += [[o2, o3, i2], [o3, i3, i2]]
    return tris

def box_tris(x0, x1, y0, y1, z0, z1):
    """Solid box triangles (outward normals)."""
    verts = [
        (x0,y0,z0),(x1,y0,z0),(x1,y1,z0),(x0,y1,z0),
        (x0,y0,z1),(x1,y0,z1),(x1,y1,z1),(x0,y1,z1),
    ]
    faces = [
        (0,2,1),(0,3,2),  # bottom
        (4,5,6),(4,6,7),  # top
        (0,1,5),(0,5,4),  # front
        (2,3,7),(2,7,6),  # back
        (1,2,6),(1,6,5),  # right
        (0,4,7),(0,7,3),  # left
    ]
    return [[verts[a], verts[b], verts[c]] for a,b,c in faces]

def subtract_box_from_mesh(tris, bx0, bx1, by0, by1, bz0, bz1):
    """Simple subtraction: remove triangles whose centroid is inside the box,
    then add the box interior faces (cap the hole). Good enough for cutouts
    that fully pierce a thin wall."""
    kept = []
    for t in tris:
        cx = (t[0][0]+t[1][0]+t[2][0])/3
        cy = (t[0][1]+t[1][1]+t[2][1])/3
        cz = (t[0][2]+t[1][2]+t[2][2])/3
        if bx0 < cx < bx1 and by0 < cy < by1 and bz0 < cz < bz1:
            continue
        kept.append(t)
    return kept

# ── Dimensions (mm) ──────────────────────────────────────────────────────────
OUTER_W  = 30.0   # width  (X)
OUTER_D  = 19.0   # depth  (Y)
WALL     = 2.5    # wall thickness
INNER_W  = OUTER_W - 2*WALL
INNER_D  = OUTER_D - 2*WALL
HEIGHT   = 68.0   # inlay height (Z)
R_OUT    = 4.0
R_IN     = R_OUT - WALL

# Button face is at X = +OUTER_W/2 (front)
# LED/window face at X = -OUTER_W/2 (back -- where WOLKENKRAFT text is)

# Button cutouts (on front face, X+)
BTNS = [
    # (y_center, z_center, y_half, z_half, label)
    (0,  HEIGHT-18, 3.5, 6.0, "fire_bar"),   # elongated fire button
    (0,  HEIGHT-34, 2.2, 2.2, "btn2"),        # small round
    (0,  HEIGHT-42, 2.2, 2.2, "btn3"),        # small round
]

# USB-C cutout at bottom center (front-to-back, Y axis)
USBC_W = 9.0
USBC_H = 4.0
USBC_Z = 1.5   # z offset from bottom

# ── Build mesh ────────────────────────────────────────────────────────────────
tris = hollow_prism(OUTER_W, OUTER_D, INNER_W, INNER_D, R_OUT, R_IN, 0, HEIGHT, n=20)

# USB-C slot (bottom, cuts through front wall)
tris = subtract_box_from_mesh(tris,
    -USBC_W/2, USBC_W/2,
    -OUTER_D/2 - 0.1, OUTER_D/2 + 0.1,
    USBC_Z, USBC_Z + USBC_H)

# Button cutouts (cut through right/left wall at X+)
for yc, zc, yh, zh, _ in BTNS:
    tris = subtract_box_from_mesh(tris,
        OUTER_W/2 - WALL - 0.1, OUTER_W/2 + 0.1,
        yc - yh, yc + yh,
        zc - zh, zc + zh)

# ── Convert to numpy-stl ──────────────────────────────────────────────────────
tri_array = np.array(tris, dtype=np.float32)  # shape (N, 3, 3)
obj = mesh.Mesh(np.zeros(len(tri_array), dtype=mesh.Mesh.dtype))
for i, t in enumerate(tri_array):
    obj.vectors[i] = t

obj.save('/home/user/AI-whispers/wolkenkraft_mini_inlay.stl')
print(f"Saved {len(tri_array)} triangles → wolkenkraft_mini_inlay.stl")
