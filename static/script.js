const outputElement = document.getElementById("output");
const inputElement = document.getElementById("input");

async function typeText(element, text, speed = 50) {
  return new Promise((resolve) => {
    let i = 0;
    function type() {
      if (i < text.length) {
        element.textContent += text[i];
        i++;
        setTimeout(type, speed);
      } else {
        resolve();
      }
    }
    type();
  });
}

async function processCommand(command) {
  appendOutput(`guest@hacker:~$ ${command}`);

  if (command === "clear") {
    outputElement.innerHTML = ""; 
    return;
  }

  try {
    const response = await fetch("/command", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command }),
    });

    const data = await response.json(); 

    const newLine = document.createElement("div");
    newLine.innerHTML = data.response; 
    outputElement.appendChild(newLine);

    outputElement.scrollTop = outputElement.scrollHeight;
  } catch (error) {
    appendOutput("Error: Unable to process command.");
    console.error("Error:", error);
  }
}

function appendOutput(text) {
  const newLine = document.createElement("div");
  newLine.textContent = text;
  outputElement.appendChild(newLine);
  outputElement.scrollTop = outputElement.scrollHeight;
}

inputElement.addEventListener("keydown", async (event) => {
  if (event.key === "Enter") {
    const command = inputElement.value.trim(); 
    if (command) {
      await processCommand(command);
    }
    inputElement.value = ""; 
  }
});

(async function showLoadingSequence() {
  const loadingMessages = [
    "Initializing system...",
    "Loading modules...",
    "Establishing secure connection...",
    "System ready."
  ];

  for (const message of loadingMessages) {
    const line = document.createElement("div");
    outputElement.appendChild(line);
    await typeText(line, message, 50); 
  }
})();
