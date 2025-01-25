const outputElement = document.getElementById("output");
const inputElement = document.getElementById("input");

// Функция для имитации печатной машинки
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

// Функция для отправки команд на сервер и обработки ответа
async function processCommand(command) {
  appendOutput(`guest@hacker:~$ ${command}`); // Отображаем введённую команду

  if (command === "clear") {
    outputElement.innerHTML = ""; // Очистка экрана
    return;
  }

  try {
    // Отправляем команду на сервер Flask
    const response = await fetch("/command", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command }),
    });

    const data = await response.json(); // Получаем JSON-ответ от сервера

    // Создаём новый элемент для вывода ответа
    const newLine = document.createElement("div");
    newLine.innerHTML = data.response; // Вставляем HTML вместо текста
    outputElement.appendChild(newLine);

    outputElement.scrollTop = outputElement.scrollHeight;
  } catch (error) {
    appendOutput("Error: Unable to process command.");
    console.error("Error:", error);
  }
}

// Функция для добавления вывода в терминал
function appendOutput(text) {
  const newLine = document.createElement("div");
  newLine.textContent = text;
  outputElement.appendChild(newLine);
  outputElement.scrollTop = outputElement.scrollHeight;
}

// Обработчик ввода команд
inputElement.addEventListener("keydown", async (event) => {
  if (event.key === "Enter") {
    const command = inputElement.value.trim(); // Получаем введённую команду
    if (command) {
      await processCommand(command); // Обрабатываем команду
    }
    inputElement.value = ""; // Очищаем поле ввода
  }
});

// Загрузка системы при запуске страницы
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
    await typeText(line, message, 50); // Анимация печатной машинки
  }
})();
