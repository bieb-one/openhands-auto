from litellm import ChatCompletionToolParam, ChatCompletionToolParamFunctionChunk

_SUM_DESCRIPTION = """Compute the sum of two numbers.
Provide numeric inputs `a` and `b` and this tool will return `a + b` as a result."""

SumTool = ChatCompletionToolParam(
    type='function',
    function=ChatCompletionToolParamFunctionChunk(
        name='sum_numbers',
        description=_SUM_DESCRIPTION,
        parameters={
            'type': 'object',
            'properties': {
                'a': {
                    'type': 'number',
                    'description': 'First addend.',
                },
                'b': {
                    'type': 'number',
                    'description': 'Second addend.',
                },
            },
            'required': ['a', 'b'],
        },
    ),
)
