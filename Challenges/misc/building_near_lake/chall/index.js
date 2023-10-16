async function submit() {
    const x = document.getElementById("input_x").value;
    const y = document.getElementById("input_y").value;
    const date = document.getElementById("input_date").value;
    const pow = document.getElementById("input_pow").value;
    const repsonse = await fetch("/verify", {
        method: "POST",
        body: JSON.stringify({
            "x": parseFloat(x),
            "y": parseFloat(y),
            "date": date,
            "pow": pow
        })
    });
    if (repsonse.ok) {
        const data = await repsonse.json();
        console.log(data);
        alert(data.data.flag);
    } else {
        alert("error!")
    }
}

async function refresh_pow() {
    const resp = await fetch("/pow");
    const data = await resp.json();
    const partialSalt = data.data.partial_salt;
    const hash = data.data.hash;
    document.getElementById("pow").innerText = `sha1(XXXX${partialSalt}) = ${hash}`;
    document.getElementById("pow").setAttribute("data-partial-salt", partialSalt);
    document.getElementById("pow").setAttribute("data-hash", hash);
}


document.getElementById("btn_submit").onclick = () => {
    submit();
    refresh_pow();
}

refresh_pow();

// Proof of Work

const pow_worker = new Worker("pow-worker.js");

let isPoWRunning = false;
pow_worker.addEventListener("message", (e) => {
    if (e.data.ok) {
        const proof = e.data.proof;
        document.getElementById("input_pow").value = proof;
        document.getElementById("pow").innerText = `${proof} 已计算完毕，请提交`;
    } else {
        document.getElementById("pow").innerText = "验证码计算失败，请检查 WebCrypto API 是否可用";
    }
    isPoWRunning = false;
});

document.getElementById("btn_spow").onclick = () => {
    if (isPoWRunning) return;
    document.getElementById("pow").innerText = "请稍等……（最多 2 分钟）";
    const partial_salt = document.getElementById("pow").getAttribute("data-partial-salt");
    const hash = document.getElementById("pow").getAttribute("data-hash");
    pow_worker.postMessage({partial_salt, hash});
    isPoWRunning = true;
};
