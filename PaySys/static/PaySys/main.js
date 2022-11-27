document.addEventListener('DOMContentLoaded', () => {
    var items = new FormData();
    // var items = {};
    var btn_count = document.querySelectorAll(".minus, .plus")
    btn_count.forEach(btn => {
        btn.addEventListener('click', e => {
            var item_id = btn.getAttribute("itemid") * 1
            if (!items[item_id]) {
                items[item_id] = 0
            }
            var offset = btn.classList.contains("minus") ? -1 : 1
            items[item_id] = Math.max(0, items[item_id] + offset)
            document.querySelectorAll('.count-item').forEach(el => {
                var _id = el.getAttribute('itemid') * 1
                if (_id === item_id) {
                    el.innerHTML = items[item_id]
                }
            })
        })
    })

    var btn_success = document.querySelector('.btn-success')
    var btn_menu = document.querySelector(".dropdown-menu");
    btn_menu.addEventListener("click", function (e) {
        if (e.target.classList.contains("btn_currency")) {
            for (let i = 0; i <= btn_menu.children.length - 1; i++) {
                if (btn_menu.children[i].classList.contains("active")) {
                    btn_menu.children[i].classList.remove("active");
                }
            }
            e.target.classList.add("active");
            btn_success.innerHTML = e.target.innerHTML
        }
    });

    var buyButton = document.getElementById('buy-button')
    buyButton.addEventListener('click', e => {
        fetch("/config/").then((result) => {
            return result.json();
        })
            .then((data) => {
                var stripe = Stripe(data.publicKey);
                var query_string = "?currency=" + btn_success.innerHTML + "&"
                for (var key in items) {
                    if (items.hasOwnProperty(key))
                        query_string += key + '=' + items[key] + '&'
                }
                query_string = query_string.substring(0, query_string.length - 1);

                fetch('/buy' + query_string, {method: 'GET'})
                    .then((response) => {
                        return response.json()
                    })
                    .then(session => stripe.redirectToCheckout({sessionId: session.id}))
            });

    })
})