// -------------------------
// Logout User
// -------------------------
function logout() {
    localStorage.removeItem("token");
}



// -------------------------
// Generate Document (DOCX / PPTX)
// -------------------------
async function generateDoc() {
    const token = localStorage.getItem("token");

    if (!token) {
        alert("Please login first!");
        window.location.href = "login.html";
        return;
    }

    const prompt = document.getElementById("prompt").value;
    const format = document.getElementById("format").value;

    if (!prompt.trim()) {
        alert("Please enter a prompt.");
        return;
    }

    try {
        const res = await fetch("http://localhost:8000/documents/generate", {
            method: "POST",
            headers: {
                "Authorization": "Bearer " + token,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt, format })
        });

        if (!res.ok) {
            const err = await res.json();
            alert("Failed: " + (err.detail || "Unknown error"));
            return;
        }

        // Download file
        const blob = await res.blob();
        const filename =
            res.headers.get("content-disposition")?.split("filename=")[1] ||
            `output.${format}`;

        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = filename.replace(/"/g, "");
        document.body.appendChild(link);
        link.click();
        link.remove();
    } catch (error) {
        alert("Error: " + error.message);
    }
}
