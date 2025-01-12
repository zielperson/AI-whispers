# SCRUM Story refinement
## Prompt
[SCRUM Story refinement](https://github.com/zielperson/AI-whispers/blob/master/SCRUM%20-%20Story%20Refinement/system.md)

## About the prompt
This is a prompt to help refine existing stories, feature requests, improvements, etc.. into a very formal SCRUM story format.

It is surprisingly resilient. You can basically throw anything at it and it makes a good story out of it.
The feature I get the most out of is the "ask me open questions" section in the end - it asks embarrassingly obvious questions at times. *(ahem)*

### Creation
This prompt was augmented by using chatGPT. It helped in the creation from the beginning until the end.

* I tasked the [recursive panelGPT](https://github.com/zielperson/AI-whispers/blob/master/PanelGPT%20recursive/readme.md) to outline a process for analyzing and writing using the [INVEST](https://www.agilealliance.org/glossary/invest/) method and [RFR model](https://trustedinstitute.com/concept/psm-i/user-stories-scrum/role-feature-reason/).
I got a nice process outline of the individual steps of analysis, and the creation of the output, in orderly steps.

* After writing the initial role and purpose, I used the process developed by the recursive panelGPT as a "Chain of Thought" instructions section. 
* In the end, the prompt describes the output and format to use.

## Notes
This is quite a restrictive prompt. 
The reason for the strict steps and output are that the output needs to be of the same quality and structure at all times.

However, the steps themselves are worded and tasked quite openly, leaving some "creative space" for your LLM of choice. 

*Special note*

Some studies have shown that a "criticize your own work" in a prompt leads to worse initial quality. 
It might be a good idea to run the part "are there open questions" as a standalone follow up.
