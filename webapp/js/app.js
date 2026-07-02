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

        <div class="timer-card"
             style="text-align:center;
                    background:#151c2e;
                    padding:14px;
                    border-radius:16px;
                    margin-bottom:20px;">

            <div style="font-size:14px;color:#9ca3af;">
                MINING TIME LEFT
            </div>

            <div id="timer"
                 style="font-size:28px;
                        font-weight:bold;
                        color:#ffffff;
                        margin-top:6px;">
                03:00:00
            </div>

        </div>

        <div class="mining-circle">

            <div style="text-align:center;">

                <div id="pickaxe"
                     style="font-size:50px;">
                    ⛏
                </div>

                <div id="liveCoin"
                     style="margin-top:14px;
                            font-size:24px;
                            font-weight:bold;
                            color:#ffb300;">
                    0.00 SHIB
                </div>

            </div>

        </div>

        <p id="mining-status"
           style="text-align:center;
                  margin-top:18px;
                  font-size:18px;
                  color:#ffd54f;">
            Ready to Mine
        </p>

        <button id="startMining">
            🚀 START MINING
        </button>

    <div class="boost-card">

    <div class="boost-title">
        ⚡ BOOST MINING REWARD ⚡
    </div>

    <div class="boost-info">

        <div class="boost-box">
            <div class="boost-label">CURRENT SPEED</div>
            <div class="boost-value" id="speedValue">1.0x</div>
            <div class="boost-green">+0% REWARD</div>
        </div>

        <div class="boost-box">
            <div class="boost-label">TOTAL REWARD</div>
            <div class="boost-value" id="rewardValue">100 SHIB</div>
            <div class="boost-small">(3 Hours)</div>
        </div>

    </div>

    <button id="watchAd">
        📺 WATCH AD TO UPGRADE
    </button>

</div>
        <div class="bottom-nav">

            <button id="homeBtn">🏠<br>Home</button>

            <button id="refBtn">👥<br>Referral</button>

            <button id="walletBtn">💰<br>Wallet</button>

            <button id="profileBtn">👤<br>Profile</button>

        </div>

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

    document
        .getElementById("pickaxe")
        .classList.add("pickaxe-rotate");

    alert(data.message);

}

async function loadBalance() {

    if (!user) return;

    try {

        const response = await fetch(`${API_URL}/balance/${user.id}`);

        const data = await response.json();

        balance = data.balance;

        const balanceElement = document.getElementById("balance");

        if (balanceElement) {
            balanceElement.innerText = balance + " SHIB";
        }

    } catch (e) {

        const balanceElement = document.getElementById("balance");

        if (balanceElement) {
            balanceElement.innerText = "0 SHIB";
        }

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
