const API_URL = "https://patio-regularly-retirement-quest.trycloudflare.com";

const tg = window.Telegram.WebApp;

tg.ready();
tg.expand();

const user = tg.initDataUnsafe.user;

let balance = 0;
let mining = null;

function loadDashboard() {

    document.getElementById("app").innerHTML = `

    <div class="dashboard">

        <header class="top-bar">

            <div class="logo">
                🐕 SHIBA MINING
            </div>

            <div class="verify">
                🟢 Verified
            </div>

        </header>

        <div class="profile-card">

            <div class="avatar">👤</div>

            <div>

                <h2 id="username">Loading...</h2>

                <p>Telegram User</p>

            </div>

        </div>

        <div class="wallet-card">

            <p>💰 Wallet Balance</p>

            <h1 id="balance">Loading...</h1>

        </div>

        <div class="mining-card">

            <h2>⛏ Mining</h2>

            <p id="mining-status">
                Checking...
            </p>

            <button id="startMining">
                🚀 START MINING
            </button>

        </div>

    </div>

    `;

    if (user) {

        document.getElementById("username").innerText =
            user.first_name + (user.last_name ? " " + user.last_name : "");

    }

}

async function startMining() {

    if (!user) return;

    const response = await fetch(`${API_URL}/start_mining`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            user_id: user.id
        })
    });

    const data = await response.json();

    alert(data.message);

}


window.onload = async () => {

    loadDashboard();

    await loadBalance();

    document
        .getElementById("startMining")
        .addEventListener("click", startMining);

};

