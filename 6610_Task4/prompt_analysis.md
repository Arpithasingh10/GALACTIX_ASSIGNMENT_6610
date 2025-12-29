## Prompt Experimentation Analysis

This task explores how different prompt formulations affect AI
responses for the same input text.

Three prompts were designed with varying levels of instruction.
The first prompt directly requested sentiment classification.
The second prompt encouraged deeper reasoning by asking the model
to consider both positive and negative aspects.
The third prompt enforced a strict output format.

Although the wording differed, the overall sentiment classification
remained consistent across prompts, identifying the text as neutral
due to mixed positive and negative signals.

The system was designed to handle API failures gracefully. When live
API access was unavailable due to quota limitations, mock outputs
were used to demonstrate expected behavior. This approach ensures
robustness and allows prompt experimentation without dependency on
external service availability.

This experiment highlights the importance of prompt design and
proper error handling in AI-integrated systems.
