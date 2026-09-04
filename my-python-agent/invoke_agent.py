import boto3
import json

client = boto3.client('bedrock-agentcore', region_name='eu-west-2')
payload = json.dumps({
    "input": {
        "prompt": "Explain machine learning in simple terms"
    }
}).encode("utf-8")

response = client.invoke_agent_runtime(
    agentRuntimeArn='arn:aws:bedrock-agentcore:eu-west-2:806766024127:runtime/strands_agent-rmyf7i6VnE',
    runtimeSessionId='test-session-123456789012345678901234567890123', # Must be 33+ char. Every new SessionId will create a new MicroVM
    contentType="application/json",
    payload=payload,
    #qualifier="DEFAULT" # This is Optional. When the field is not provided, Runtime will use DEFAULT endpoint
)
response_body = response['response'].read()
response_data = json.loads(response_body)
print("Agent Response:", response_data)