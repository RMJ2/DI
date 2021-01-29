        //sidenav
        const sideNav = document.querySelector('.sidenav');
        M.Sidenav.init(sideNav, {});

        //slider
        const slider = document.querySelector(".slider");
        M.Slider.init(slider, {
            indicators: false,
            height: 500,
            transition: 500,
            interval: 6000
        });

        // autocomplete
        const ac = document.querySelector('.autocomplete');
        M.Autocomplete.init(ac, {
            data: {
                "HTML": null,
                "CSS": null,
                "JAVASCRIPT": null,
                "DOM": null,
                "PYTHON": null,
                "GITHUB": null,
                "JSON": null,
                "APIs": null,
                "WEB SERVERS": null,
                "FLASK FRAMEWORK": null,
                "DJANGO": null,
                "SQL": null,
                "HEROKU": null,
                "AWS": null,
                "DEVELOPERS INSTITUTE": null,

            }
        });

        // Material Boxed
        const mb = document.querySelectorAll('.materialboxed');
        M.Materialbox.init(mb, {});

        //scrollspy
        const ss = document.querySelectorAll('.scrollspy');
        M.Scrollspy.init(ss, {});


        // Fade-In
        window.onload = function () {
            window.setTimeout(fadein, 1500); //1.5 seconds
        }
        function fadein() {
            document.getElementById('fadeIn').style.opacity = '1';
        }
        let buttonYes = document.getElementById('btnYes')
        let buttonNo = document.getElementById('btnNo')
        buttonYes.addEventListener("click", welcome)
        buttonNo.addEventListener("click", goodBye)
        let msg=document.getElementById('fadeIn')
        function goodBye(){
            msg.innerText='What are you doing with your life'
        }
        function welcome(){
          msg.innerText='Well then ,share your ideas with us!'
          setTimeout(clearWelcome,2000)
        }
        function clearWelcome(){
            msg.style.opacity='0'
        }

