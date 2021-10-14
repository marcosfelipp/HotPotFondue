document.getElementsByClassName('card-flavor')[0]
        .addEventListener('click', function (event) {
            console.log('aa')
            document.getElementById('div-card-2').setAttribute("class", "flavor-selected");
        });

