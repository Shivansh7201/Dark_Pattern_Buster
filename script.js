//current_url=window.location.href;
const current_url = "https://www.flipkart.com/"
const url="https://localhost:4040/predict?url="+current_url;
async function fetchData() {
    const res=await fetch(url);
    const record=await res.json();
    document.getElementById("pattern").innerHTML=record;
}
fetchData();
