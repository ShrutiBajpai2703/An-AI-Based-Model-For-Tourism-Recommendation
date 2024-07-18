const option1 = document.getElementById("option1");
const option2 = document.getElementById("option2");
const option3 = document.getElementById("option3");

option1.addEventListener("click", () => {
  hideOptions();
  document.getElementById("option1-suboptions").style.display = "block";
  document.querySelector("#option1-suboptions button:nth-child(1)").addEventListener("click", () => {
    const chatBody = document.querySelector(".chat-body");
    const response = document.createElement("p");
    response.innerText = "You selected Option 1-1.";
    chatBody.appendChild(response);
  });
});

option2.addEventListener("click", () => {
  hideOptions();
  document.getElementById("option2-suboptions").style.display = "block";
});

option3.addEventListener("click", () => {
  hideOptions();
  document.getElementById("option3-suboptions").style.display = "block";
});

function hideOptions() {
  const suboptions = document.querySelectorAll(".options[id$='-suboptions']");
  suboptions.forEach((suboption) => {
    suboption.style.display = "none";
  });
}
