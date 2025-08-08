function sendMessage() {
  const input = document.getElementById('userInput');
  const message = input.value.trim();
  if (message === '') return;

  const chatWindow = document.getElementById('chatWindow');

  // Show user's message
  const userDiv = document.createElement('div');
  userDiv.className = 'message user';
  userDiv.textContent = message;
  chatWindow.appendChild(userDiv);

  // Show "Typing..." message from bot
  const botDiv = document.createElement('div');
  botDiv.className = 'message bot';
  botDiv.textContent = 'Typing...';
  chatWindow.appendChild(botDiv);
  chatWindow.scrollTop = chatWindow.scrollHeight;

  // Prepare form data to send
  const formData = new FormData();
  formData.append("query", message);

  // Send POST request to FastAPI
  fetch("http://127.0.0.1:8000/web_search_result/", {
    method: "POST",
    body: formData
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    botDiv.textContent = '';
    const responseText = data.search_result || "Sorry, I couldn't find anything.";
    const urls = data.urls || [];

    // Typing effect for the response
    const words = responseText.split(" ");
    let i = 0;
    const interval = setInterval(() => {
      if (i < words.length) {
        botDiv.textContent += words[i] + " ";
        i++;
        chatWindow.scrollTop = chatWindow.scrollHeight;
      } else {
        clearInterval(interval);

        // After typing completes, show URLs
        if (urls.length > 0) {
          const urlsDiv = document.createElement('div');
          urlsDiv.className = 'message bot';
          urlsDiv.innerHTML = `<strong>Related Links:</strong><br>` +
            urls.map(url => `<a href="${url}" target="_blank" style="color: lightblue;">${url}</a>`).join('<br>');
          chatWindow.appendChild(urlsDiv);
          chatWindow.scrollTop = chatWindow.scrollHeight;
        }
      }
    }, 80);
  })
  .catch(error => {
    console.error("Error:", error);
    botDiv.textContent = "❌ Error processing your query.";
  });

  input.value = '';
}

function processLink() {
  const link = document.getElementById("linkInput").value;
  const chatWindow = document.getElementById("chatWindow");

  if (!link.trim()) {
    alert("Please enter a link.");
    return;
  }

  // Show "Processing..." message from bot
  const linkMsg = document.createElement("div");
  linkMsg.className = "message bot";
  linkMsg.textContent = 'Processing...';
  document.getElementById("linkInput").value = "";
  chatWindow.appendChild(linkMsg);
  chatWindow.scrollTop = chatWindow.scrollHeight;

  const formData = new FormData();
  formData.append("url", link);  // Make sure the key is "url" to match FastAPI

  fetch("http://127.0.0.1:8000/process_link/", {
    method: "POST",
    body: formData,
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Server error: ${response.statusText}`);
      }
      return response.text();  // Since FastAPI returns plain text
    })
    .then((data) => {
      linkMsg.textContent = '';
      linkMsg.textContent = data;  // 🔗 Link processed or ❌ Error: ...
      chatWindow.scrollTop = chatWindow.scrollHeight;
    })
    .catch((error) => {
      linkMsg.textContent = '';
      linkMsg.textContent = "❌ Error processing link.";
      chatWindow.scrollTop = chatWindow.scrollHeight;
    });
}

function linkResponse() {
  const input = document.getElementById('userInput');
  const message = input.value.trim();
  if (message === '') return;

  const chatWindow = document.getElementById('chatWindow');

  // Show user message
  const userDiv = document.createElement('div');
  userDiv.className = 'message user';
  userDiv.textContent = message;
  chatWindow.appendChild(userDiv);

  // Show "Typing..." message from bot
  const botDiv = document.createElement('div');
  botDiv.className = 'message bot';
  botDiv.textContent = 'Typing...';
  chatWindow.appendChild(botDiv);
  chatWindow.scrollTop = chatWindow.scrollHeight;

  // Prepare form data
  const formData = new FormData();
  formData.append("query", message);

  fetch("http://127.0.0.1:8000/link_response/", {
    method: "POST",
    body: formData,
  })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Server error: ${response.statusText}`);
      }
      return response.text(); // Plain text response expected
    })
    .then(data => {
      botDiv.textContent = ''; // clear "Typing..."

      const words = data.split(" ");
      let i = 0;

      const interval = setInterval(() => {
        if (i < words.length) {
          botDiv.textContent += words[i] + " ";
          i++;
          chatWindow.scrollTop = chatWindow.scrollHeight;
        } else {
          clearInterval(interval);
        }
      }, 80);
    })
    .catch(error => {
      console.error("Error:", error);
      botDiv.textContent = "❌ Error processing your query.";
    });

  input.value = '';
}
