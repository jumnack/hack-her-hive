function encrypt() {
    var input = document.getElementById("input-code").value;
    var encrypted = btoa(input);
    document.getElementById("output-code").value = encrypted;
}

function decrypt() {
    var input = document.getElementById("output-code").value;
    var decrypted = atob(input);
    document.getElementById("input-code").value = decrypted;
}
