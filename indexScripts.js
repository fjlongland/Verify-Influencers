document.addEventListener("DOMContentLoaded", async function(){

    fetchLeaderboard()

})

async function fetchLeaderboard(){
    try{
        const response = await fetch("https://verify-influencers-production.up.railway.app/post/LB", {
            method: 'GET',
        });
        if(!response.ok){
            throw new Error("HTTP error: status: "+ response.status);
        }
        const data = await response.json();
        console.log("raw data: ", json.stringify(data));

    }
    catch(error){
        console.error("Error fetching leaderboard: ", error);
    }
}

function searchClicked() {
    var name = document.getElementById('influencerName').value;
    document.cookie = "cName=" + name + "; path=/";
    const test = getCookie();
    console.log("it worked: "+test)
}
function getCookie(){
    const cookieStr = document.cookie;
    if(cookieStr){
        const [name, value] = cookieStr.split('=');
        if (name.trim()==='cName'){
            return decodeURIComponent(value);
        }
    }
    return null;
}