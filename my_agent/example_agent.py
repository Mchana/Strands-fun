import logging
from strands import Agent
from strands.models import BedrockModel

#create logging
logging.getLogger("strands").setLevel(logging.DEBUG)

#logging config
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)


bedrock_model = BedrockModel(
    model_id="global.anthropic.claude-sonnet-4-6",
    region_name="eu-west-2",
    temperature=0.3,
)

#set agent and model
#agent = Agent(model="global.anthropic.claude-sonnet-4-6")
agent = Agent(model=bedrock_model)
#invoke agent with a request
agent("Hello! Don't eat me :(")

#prints what model it is
#print(agent.model.config)