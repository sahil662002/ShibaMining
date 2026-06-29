const tg = window.Telegram.WebApp;

tg.ready();
tg.expand();

const user = tg.initDataUnsafe.user;

const app = document.getElementById("app");

app.innerHTML = `
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

        <div class="avatar">
            👤
        </div>

        <div>
            <h2 id="username">Loading...</h2>
            <p>Telegram User</p>
        </div>

    </div>

    <div class="wallet-card">
        <p>💰 Wallet Balance</p>
        <h1 id="balance">0 SHIB</h1>
    </div>

    <div class="mining-card">

        <h2>⛏ Mining</h2>

        <p id="mining-status">
            Ready To Start
        </p>

        <button id="startMining">
            🚀 START MINING
        </button>

    </div>

    <div class="bonus-card">

        <h2>🎁 Daily Bonus</h2>

        <p>Coming Soon</p>

    </div>

    <nav class="bottom-nav">

        <button>🏠<br>Home</button>

        <button>👥<br>Referral</button>

        <button>💰<br>Wallet</button>

        <button>👤<br>Profile</button>

    </nav>

</div>
`;

if (user) {

    document.getElementById("username").innerText =
        user.first_name + (user.last_name ? " " + user.last_name : "");

}
