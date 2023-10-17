addEventListener('message', function (e) {
    const { partial_salt, hash } = e.data;
    solve_pow(partial_salt, hash).then(proof => {
        postMessage({ ok: true, proof });
    }).catch(err => {
        postMessage({ ok: false, proof: null });
    });
});

async function solve_pow(partial_salt, hash) {
    const letters = "abcdefghijklmnopqrstuvwxyz";
    for (let i of letters) {
        for (let j of letters) {
            for (let k of letters) {
                for (let l of letters) {
                    const proof = await crypto.subtle.digest("SHA-1", new TextEncoder().encode(`${i}${j}${k}${l}${partial_salt}`));
                    const proof_hex = Array.from(new Uint8Array(proof)).map(b => b.toString(16).padStart(2, '0')).join('');
                    if (proof_hex === hash) {
                        return `${i}${j}${k}${l}${partial_salt}`;
                    }
                }
            }
        }
    }
}
