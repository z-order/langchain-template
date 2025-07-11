// install first:
//   pnpm i @langchain/langgraph-sdk
import { Client } from "@langchain/langgraph-sdk";

// override console.log to print objects to the fullest depth
const myconsole = new console.Console({
  stdout: process.stdout,
  stderr: process.stderr,
  inspectOptions: {
    depth: null, // null: this will ensure objects are logged to the fullest depth, 5: this will ensure objects are logged to the depth of 5
    colors: true, // enabling colored output; you can skip this or adjust as needed
  },
});
console.log = myconsole.log;

// 1 · Connect to the locally running LangGraph-CLI server
const urlForCliDeployment = "http://localhost:8123";
const client = new Client({ apiUrl: urlForCliDeployment });

// 2 · Start an empty thread (persists graph state between runs)
const thread = await client.threads.create();

// 3 · Prepare user inputs, per-run config, and the graph / assistant name
const userInput1 = "Add a ToDo to follow-up with DI Repairs.";
const userInput2 = "Add a ToDo to mount dresser to the wall.";
const config     = { configurable: { user_id: "Test-Double-Texting-JS" } };
const assistantId = "task_maistro";   // must match the graph name you deployed

// 4 · Kick off the first run on the thread
const run1 = await client.runs.create(
  thread.thread_id,
  assistantId,
  {
    input: {
      messages: [
        { role: "user", content: userInput1 }
      ]
    },
    config,
    multitaskStrategy: "enqueue",
    onCompletion: "continue",
    onDisconnect: "continue"
  }
);
console.log("Run created:", run1, '\n\n');

const run2 = await client.runs.create(
  thread.thread_id,
  assistantId,
  {
    input: {
      messages: [
        { role: "user", content: userInput2 }
      ]
    },
    config,
    multitaskStrategy: "enqueue",
    onCompletion: "continue",
    onDisconnect: "continue"
  }
);
console.log("Run created:", run2, '\n\n');

// 5 · Wait for the run to complete
const result1 = await client.runs.join(thread.thread_id, run1.run_id);
console.log("Run result:", result1, '\n\n');

const result2 = await client.runs.join(thread.thread_id, run2.run_id);
console.log("Run result:", result2, '\n\n');
