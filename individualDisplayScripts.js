document.addEventListener("DOMContentLoaded", async function(){
    const name = getCookie();
    console.log(name);

    fetchInfo(name);

})

async function fetchInfo(name) {
    try{
        const response = await fetch("https://verify-influencers-production.up.railway.app/post/ai/"+name, {
            method: 'GET',
        });
        if (!response.ok){
            throw new Error("HTTP error: status: "+ response.status);
        }
        const data = await response.json();
        console.log("raw data: ",  JSON.stringify(data));

        const {fields, summary} = data.data;

        const fieldstr = fields.join("    ");

        const aboutstr = fieldstr+"\n\n"+summary;

        document.getElementById("nameDisplay").textContent = name;

        document.getElementById("about").value = aboutstr;
        document.getElementById("trustScore").value = data.data.reliability_score;
        document.getElementById("yearlyRev").value = data.data.yearly_revenue;
        document.getElementById("products").value = data.data.products_released.total;
        document.getElementById("followers").value = data.data.online_followers.total;

        const formattedClaims = formatClaims(data)

        console.log(formattedClaims)

        document.getElementById("healthClaims").value = formattedClaims;


    }
    catch(error){
        console.error("Error fetching data: ", error);
        if (error instanceof TypeError && error.message.includes('CORS')){
            console.error("CORS error detected. Check server configuration and allowed origins.")
        }
    }
        
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

function formatClaims(data) {
    // Check if data has the expected structure
    if (!data || !data.claims || !data.claims.claims || !Array.isArray(data.claims.claims)) {
        console.error("Unexpected data structure:", data);
        return "No claims data available";
    }

    const claims = data.claims.claims;
    let result = "";

    claims.forEach((claim, index) => {
        result += `
CLAIM: ${index + 1}: ${claim.Claim}

BRIEF: ${claim.brief}

SOURCE: ${claim.source}

CLAIM DETAILS: ${claim.claim}

EVIDENCE:
    - Source: ${claim.medicalEvidence?.source}
    - Excerpt: ${claim.medicalEvidence?.excerpt}

VERDICT: ${claim.verdict}



`;
    });

    return result || "No claims data available";
}