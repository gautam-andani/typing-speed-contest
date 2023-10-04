let startTime;
const startTimer = () => {
    startTime = new Date().getTime();
}

document.querySelector("form").addEventListener("submit", () => {
    const endTime = new Date().getTime();
    const completionTime = endTime - startTime;
    document.getElementById("completion_time").value = Math.floor(completionTime/100);
});