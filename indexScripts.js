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
        console.log("raw data: ", JSON.stringify(data));

        leaderboard = formatLeaderBoardData(data);

        console.log(leaderboard);

        document.getElementById("leaderboard").value = leaderboard;

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

function formatLeaderBoardData(data) {
    // Check if data has the expected structure
    if (!data || !data.data || !data.data.influencers || !Array.isArray(data.data.influencers)) {
        console.error("Unexpected data structure:", data);
        return "No leaderboard data available";
    }

    const influencers = data.data.influencers;
    let result = "Name            Trust Score     Followers   \n";
    result += "------------------------------------------\n";
    
    influencers.forEach(inf => {
        result += `${inf.name.padEnd(15)} ${inf.trustScore.toString().padEnd(15)} ${inf.totalFollowing.toLocaleString().padEnd(12)}\n`;
    });
    
    return result;
}