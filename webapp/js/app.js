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

        <div class="mining-circle">

            <div>

                <div style="font-size:42px;">⛏</div>

                <div id="timer"
                     style="margin-top:12px;font-size:20px;font-weight:bold;">
                    03:00:00
                </div>

            </div>

        </div>

        <p id="mining-status">
            Ready to Mine
        </p>

        <button id="startMining">
            🚀 START MINING
        </button>

        <p id="balance"
           style="text-align:center;
                  margin-top:20px;
                  font-size:22px;
                  color:#ffb300;
                  font-weight:bold;">
            0 SHIB
        </p>

    </div>

    `;

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

async function loadBalance() {

    if (!user) return;

    try {

        const response = await fetch(`${API_URL}/balance/${user.id}`);

        const data = await response.json();

        balance = data.balance;

        document.getElementById("balance").innerText =
            balance + " SHIB";

    } catch (e) {

        document.getElementById("balance").innerText =
            "0 SHIB";

        console.log(e);

    }

}

window.onload = async () => {

    loadDashboard();

    await loadBalance();

    document
        .getElementById("startMining")
        .addEventListener("click", startMining);

};

