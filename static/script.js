function processNote() {
  const note = document.getElementById("noteInput").value;

  // Send note for summarization
  fetch("/summarize", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ note: note }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("summary").textContent = data.summary;
    });

  // Send note for categorization
  fetch("/categorize", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ note: note }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("categories").textContent =
        data.categories.join(", ");
    });
}
