async function loadMatches() {

    const container = document.getElementById("matches");

    try {

        const response = await fetch("./matches.json");
        const data = await response.json();

        container.innerHTML = "";

        data.matches.forEach(match => {

            const bdTime = new Date(match.date).toLocaleString(
                "en-BD",
                {
                    timeZone: "Asia/Dhaka",
                    dateStyle: "medium",
                    timeStyle: "short"
                }
            );

            container.innerHTML += `
            <div class="match-card">

                <div class="stage">
                    ${match.stage}
                </div>

                <div class="teams">
                    ${match.home} vs ${match.away}
                </div>

                <div class="time">
                    🇧🇩 ${bdTime}
                </div>

            </div>
            `;
        });

    } catch (error) {

        container.innerHTML = `
        <div class="loading">
            Failed to load matches
        </div>
        `;

        console.error(error);
    }

}

loadMatches();
