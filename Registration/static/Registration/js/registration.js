// registration.js
console.log("registration.js loaded");

function addMember(e) {
    e.preventDefault();

    const container = document.getElementById("team-members");
    const max = parseInt(container.dataset.max);

    if (container.children.length >= max) {
        alert("Maximum team size reached");
        return;
    }

    const div = document.createElement("div");
    div.innerHTML = `
        <input type="text" name="team_members[]" placeholder="Member Name" required>
        <button type="button" class="remove-btn">Remove</button>
    `;

    container.appendChild(div);
    attachRemoveEvents();
}

function removeMember(e) {
    const container = document.getElementById("team-members");
    const min = parseInt(container.dataset.min);

    if (container.children.length <= min) {
        alert("Minimum team size required");
        return;
    }

    e.target.parentElement.remove();
}

function attachRemoveEvents() {
    document.querySelectorAll(".remove-btn").forEach(btn => {
        btn.onclick = removeMember;
    });
}

/* 🔥 MIN TEAM SIZE CHECK ON SUBMIT */
function validateTeamSize(e) {
    const container = document.getElementById("team-members");
    if (!container) return;

    const min = parseInt(container.dataset.min);
    const count = container.children.length;

    if (count < min) {
        e.preventDefault();
        alert(`Minimum ${min} team members required`);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    document
        .getElementById("add-member-btn")
        ?.addEventListener("click", addMember);

    document
        .querySelector("form")
        ?.addEventListener("submit", validateTeamSize);

    attachRemoveEvents();
});
