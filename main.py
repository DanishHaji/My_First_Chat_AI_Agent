from agents import Agent, AsyncOpenAI, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from agents.run import RunConfig
import os
from dotenv import load_dotenv

set_tracing_disabled(disabled=True)
load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")


external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


model = OpenAIChatCompletionsModel(
    model="models/gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
)

agent = Agent(
    name="GeminiAgent",
    instructions="You are a helpful assistant. Answer questions accurately.",
    tools=[]  # no tools
)

result = Runner.run_sync(agent, "who is the founder of Pakistan ? and what is the population of Pakistan ?", run_config=config)

print(result.final_output)