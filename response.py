 <py-script>
        from pyscript import Element # Mengimpor Element dari PyScript untuk manipulasi DOM

        def respond(event): # Fungsi untuk menangani respons chatbot
            user_input = Element('userInput').element.value.lower() # Mengambil input pengguna dan mengubahnya menjadi huruf kecil
            if "halo" in user_input: # Menanggapi jika input mengandung "halo"
                response = "Halo ada yang bisa saya bantu?"
            elif "hai" in user_input: # Menanggapi jika input mengandung "hai"
                response = "Haii ada yang bisa saya bantu?"
            elif "apa kabar" in user_input: # Menanggapi jika input mengandung "apa kabar"
                response = "Saya baik-baik saja, terima kasih!"
            elif "rekomendasi" in user_input: # Menanggapi jika input mengandung "rekomendasi"
                response = "Hewan peliharaan apa yang anda miliki?"
            elif "kucing" in user_input:
                response = """
                Berikut rekomendasi nama untuk kucing Anda:
                <div style='display: flex; justify-content: space-between;'>
                    <div style='width: 50%;'>
                        <ul>
                            <li>Milo</li>
                            <li>Neko</li>
                            <li>Kiki</li>
                            <li>Loki</li>
                            <li>Tara</li>
                        </ul>
                    </div>
                    <div style='width: 50%;'>
                        <ul>
                            <li>Whiskers</li>
                            <li>Oliver</li>
                            <li>Leo</li>
                            <li>Ginger</li>
                            <li>Shadow</li>
                        </ul>
                    </div>
                </div>""" #Membuat respons dengan 2 kolom nama
            
            elif "anjing" in user_input:
                response = """
                Berikut rekomendasi nama untuk anjing Anda:
                <div style='display: flex; justify-content: space-between;'>
                    <div style='width: 50%;'>
                        <ul>
                            <li>Chiko</li>
                            <li>Belo</li>
                            <li>Snowy</li>
                            <li>Midnight</li>
                            <li>Simba</li>
                        </ul>
                    </div>
                    <div style='width: 50%;'>
                        <ul>
                            <li>Buddy</li>
                            <li>Daisy</li>
                            <li>Rocky</li>
                            <li>Max</li>
                            <li>Charlie</li>
                        </ul>
                    </div>
                </div>"""
            
            elif "burung" in user_input: # Menanggapi jika input mengandung "burung"
                response = """
                Berikut adalah rekomendasi nama untuk burung:
                <div style='display: flex; justify-content: space-between;'>
                    <div style ='width: 50%;'>
                        <ul>
                            <li>Sky</li>
                            <li>Sunny</li>
                            <li>Lola</li>
                            <li>Kiwi</li>
                            <li>Pepper</li>
                        </ul>
                    </div> 
                    <div style='width: 50%;'>
                        <ul>
                            <li>Pixel</li>
                            <li>Echo</li>
                            <li>Nox</li>
                            <li>Vega</li>
                            <li>Zara</li>
                        </ul>
                    </div> 
                </div>"""
            elif "ikan" in user_input: # Menanggapi jika input mengandung "ikan"
                response = """
                Berikut rekomendasi nama untuk ikan anda:
                <div style='display: flex; justify-content: space-between;'>
                    <div style='width: 50%;'>
                        <ul>
                            <li>Lucky</li>
                            <li>Nemo</li>
                            <li>Bubbles</li>
                            <li>Suki</li>
                            <li>Yoda</li>
                        </ul>
                     </div>
                    <div style='width: 50%;'>
                        <ul>
                            <li>coco</li>
                            <li>jett</li>
                            <li>Zylo</li>
                            <li>Riptide</li>
                            <li>Aqua</li>
                        </ul>
                    </div>
                </div>"""
            elif "kata" in user_input:
                response="Bekerjalah untuk suatu tujuan,bukan pujian.Jalanilah hidup untuk berekspresi, bukan untuk mengesankan - J.R.R. Tolkien"
            elif "lagi" in user_input: # Menanggapi jika input mengandung "kata"
                response = "jangan bergantung pada orang lain apalagi bergantung di pohon sambil makan pisang"
            elif "lanjut" in user_input: # Menanggapi jika input mengandung "lagi dong"
                response = "Kegagalan bukan untuk ditakuti, melainkan untuk dipelajari"
            else: # Menanggapi jika input tidak dikenali
                response = "Maaf, saya tidak mengerti."

        
                # Update chat output with user and bot messages alongside profiles
            Element('chatOutput').element.innerHTML += f"""
                <div class='message user-message'>
                    <div class='profile'>
                        <img src='https://t4.ftcdn.net/jpg/02/29/75/83/360_F_229758328_7x8jwCwjtBMmC6rgFzLFhZoEpLobB6L8.jpg' alt='User Profile' class='profile-pic'>
                        <span>USER</span>
                    </div>
                    <span>{user_input}</span> <!-- Display user message text -->
                </div>
            """
            Element('chatOutput').element.innerHTML += f"""
                <div class='message bot-message'>
                    <div class='profile'>
                        <img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJQAAACUCAMAAABC4vDmAAAA2FBMVEX///8AAAD19fVgfYvP2Nyenp74+Pj8/Px/jpTy8vI3R09kgpHk5ORkZG
                        SqqqpadYIaIiZaWlqkpKR5h41fX18WFhY+Pj7R0dGGhobGxsa/v7/W3+Ps7Oxra2vc3NxJSUkcHByTk5N9fX0nJycyMjK2trYqLjAODg4qNjxIXmgAvNRSUlJ0dHQCqvZTbXkSFxo/UltV
                        XWEAFB0BkdHCy89pdXoALkMBfbQBnuQAQ2EANk4Bbp8ADBEBWoIAJzgAMjgAi50AJSkAbnwAYGwATVcAn7MAGBsAP0h/wDqoAAAO3UlEQVR4nMVcbWOiSBJWRyAYxEBUFBHEN+LJGLOT7M
                        zd5m7n9uX2//+jo6v6DQSF1sw+X5IIwkN19VNV3UVarQK85ardduyg+LmAbnlTdzIcL5J2htHaWca+Z5nVXzD8NGknw82ZU87CSNuI8bTqBhNn3T7Fap9WPYg5p+dEoRKnzl7cpoRV6Dsl
                        fCRmrmeccpJO8FRIxdIF1lbhIAzsBSRDu0DLWEqHo1POF2Et4Ks//wQ/YvlQZzMuEliMx1E0PiUa557Gww9/focfdnNSNvneT1+/ffsn+WUkHdlE8m3HfXfjhZYVBIFlhaFvL6NEOryNO+
                        KbYPyfvnz78i/yy7y5qeACv3z+/Pnbf8hvfLZMJUrDyZRYwtAzdDod8sPI7mR62vxdnOXq7LvghV/JNckv6+YzcEK+9yW7wGcwFZ1NpvCKtRaahkHIFJFR64TumBssYj5NnucdrkmcYtWc
                        lEYu9+/s+1/Aq/BpNwt2o3RqtMoICWLBdMn1IsaR6jPrf4GB75y7fyk25Hvvv3z7AqO3Jh/pE3qPJA0zY1xE+Boz13dAlsBP379++wrXXDbm1OrkZHGTfWIxb5qHZ40krBXMXid0EBOfXC
                        E3PSsk+bKp2INmw+9RluupXosSgTmbvfbpNbQW9Qk2SxQ4yeq5ytx8Sn+fmDUGTmDWnWnUPhODehV6v2L0s/FqydzidltPS+cbqIFeakGrO3ul454aLUPDqbJIm3s5hQnKTZTXx8vurVap
                        PQzLA5TRCrqzLhWSZWarkDBMlAIfBaidx+2Udsq9ydASxDAoZdWdUVdIM6UdZj9HynYSpGjMmlRw0r0R8xS7zOEIK5t5u06uOVJNpwSpEOfdpHzoMlJsEhCVLDsBWKE2uK2bkEpC9NNJtR
                        AEXNOm5SdZwlZh/xakRpinzKvsREwVpEOC/rRCLvRZxsrF+bu+yfBRWTkb6VqgCK1qCSOsJvxqtyG1OMfJ6JgcVWpvdjNWzm1J+Wdk3LD7ApMyUSC2zJy9+7q+JanySUU5uW0Z+6pTibP7
                        NyS1Ko8tlFQ/R6pddSoMYHo7Ut65GGzEOU6rynMzU3W70a1IpWfzAt2SCsT2qEKpiKlmXK1uQOqsGhA9sATOZKTg67PoalIwW8rCCxYuDNI3xIclqUyXm+qKLAGSg7VVvLbR6liev7EvwP
                        dCMy+nYCqSJajk5+ypYTVikh8Q3dC9iTMetS8j2e7TjSnNXPAqeNKkuA5QGyFcOmco3fDi5CyTE6TTDnssnUzAGcRSV5UUpPlD2aMMq8bCxonB9h6zFmgVXHasSgoeaSNGT9e187evtpaF
                        VyHZAgYb1YTYI+M0FqNnWEN+l+eHp6feBTw9iIEe0+AJrg6uqqmRgpgmhNPw2Mg993aD+zo49LbPjJZr8PGDC/f1ywxOgXOPpweGTzk97Aaf7j/VxK73xGjhLCbj14W/z6ykViMA4zM78W
                        L0WJ9RhsxYvSc6iiTVAKfCvEqlascSxqGG0r0tmunQgBFj1XsQIwhOFZO/lPRTY08H8oTp2dOgiZkEK3wiyDZ4qFESBUiTqCAYmF4/NWUErHZkJsL3o6Cjd5kobFWCMlGplQeCYKBDPahw
                        ynDktspie8hShZGCUgVkso0x40YZTQaKpAY97leWAZEGR6E5KSjF9x3JUDvuT0SDapBhp8EA9mAOLg3w9ImifEKOn2LgG+Yd6pCNx/HyNBxkInXcwdToMbdahEI+J81J2dQHiByAoQ5onP
                        sBOm3ydF6w7o/PVGvviYYyU8Xo6RgsGpNy0cLEo8DYW8ppx+JG+/lwjtUTP69HvQo+GbVmjJTTPNBoXBFaK8mjBjyYZayqSd33xGntXWY2bqqQk1JYsgbVJQsWugWjMCgagNigitX9QT6t
                        PQAFxQmoQaVF+KnuOBBShi+5+QBu8uv37/+VmVYZ6rfvv9N5K8YvhZA8upYU2Ox4Lzzq139kAFZVU3AARvmenfYbPBGSAqYO4dQlHqGwDSJIpcKl7o9gAELqD/SWc6TIaX/+j1j0HlQdSI
                        1fCanFTUihTSRSf9Uj9b1dILXipBSCH3f0DiR71HvAgd//pDdLKhUU3Od3xv2JkiLuPfKvcHQuCWZfIvUJFeGvX9uS95c4Oli0/f4Hzr4DJUW+nPhXSAIXT1221KejPNV31UIln0a45y2l
                        Kp48zFCfYveXhOrpjHgK4cdBzvuUapjhARkTPG6UAWfVq6SUY/UMjsdJRa8s9VQIyJC6ODpZ0gQGIm/ZEVrJE6NZSGPYn5k0ERd6OEKaIMTzhSfp8WUSRcCGYWSSeo9cYSvfeHA4iDKrtz
                        1KlA7bLdeJwYCfBmEGsk+i6FiOKrQAQKkA6bCOM6himMidng60+hz0yk/FNA/EyyWkyNpfolJjQXHmZ6Ra+/z45YG+/NDb7XZHWniWnMpHr80Lh5XKahCMu0YkHVeUyjnl5n6lUogkwYEl
                        KtBOBU5YEu8hd4G64Vhuqt3JclWJUvC5195wP5+rkArgImQRFkXhuTxPyVy7YKfTc0Q5E0GFBf7gq5BCJSeBRg+qLECNxddWEqoABd5H7lG2xaSzrbbACNGvb/AsvTKq3H867Mh9j7tDaT
                        Fx4LnwyuC1jEMjnzW1Xdv36oackMjnKiSiEERnWSG1qoMDFouzrINUfV0YPaj6jHhEXXK0jr1aAXrM5h8rR5Oz9UsVjpzThBiqC3MvgT4TL+eNTp3VWdxjN6Fwp6udx8scSjjRFaoIy2NI
                        hfbCQyRsL5fyATQ2uFAl67TDr9dozewT1KGUU+YJRKTQzVHOvXYRy4vOFZPT6I6DQXe0kl0DWveDI19fXFlgqC6sAeyp/2wcJ00ny7TPt8ZXl9oaUQpwb0bn3ZDbbNrX43V/OD7RVbz2wj
                        N0sTfDg7FOLWNN53VZxWhqXDmjfxE8ZLN/cAmHQ0+U045p4IYf/FW6itdhXWwXWGHDAV2lomUpw/PDBcjxJ84ig7Q1WqHmtBPkUqKFNPZ0K8QwJw03ZhB9r9WRuwAq12CxcrqYkg4pd7YR
                        EqbV967AeGoauFk0o4088hK6MdUmsc8+MZ06OyTYrZSRp7sheivQhnX21Sj2Ew/2/HSp30UavCnbWRnbbD5qNVb9qZTEfJtTN8zQj4eLchISkmi58QKdb8rM7BF9QG4luW3XadLizHunpO
                        2susUR21LTpR4qkUdZhW7fJvmxy56kUTNeDqTbjDpjnxfr5j7PicbDmmARyu4o0rIyF6eS7YjL0rEbD+d92m68aFKesu5KxzvXylEF08rMRKUkFYsauBm8WGqu62oxcm60ij1lW31Lz2hq
                        LakDNadAkCysYldDQMY2brTfFrBu2NF82mlgLl2f+XzbOZGFHIPFknHScBo02xqRen8izTPOtG9JjFpGqIm+sDSXlUPauNY4XDixaSkfiu6fxTj2gkwYKk1G2js6pufuxd782M97Mfip4w
                        pW4PfN6y5fnsOL4cSeWnAj2kOCnSZwphVu4lRWoYVbTMBxI1kiNSlMzrowpk4uwiSr9bg/0UgDCcLzbS1Oo/Uqr/dj7bQmsEstlTYnlaFxA0c2JJuyMsVHtsKnIAoqrFkBjGYdE/uKWQ6zL
                        xGzT4OHVWyhKDSWXYZTUQqDy600ysoFf10r9QUIwaqPRVme2aGhcDtxCWK8rMLiXounVxnGDrRQgrosxgwgAWs8ImbfKasOzxWTfbpcOlQ6lJqvdSoKfd/EnjKMYJFLYdN0Fo4FXX+ON1s
                        UXaWYtFCoeRT1cZ933ulIik8hSgqPzbozH4clyl9mU97vpLQ41LLwDpaU7p0hhaUCjpMc/lloSN4eZYPtFWceZkBysneeVMA7O8c8ZdFjJqxvd3d3b1xlXcWGRgsCe645/zwpKD9f4b64c
                        mF4MSOxfrwDsMJEFSjCZueEFBdmF0Ym5qREDxcp9QJNekMlxylSf+eBtjjk8wG4aMxYwT1ES7bJ9/sXsdxivH1DSo+YcC6u6EXFNx7y6QoK895GQ6HTSd3fsGF8Mv9fqJket9dMO4ABGUK
                        Qz5xwkb29h0wbZ5ojbAk9XN15jtH25Y7iLbmaU8sASxdI6QHaYe3M+9Qivp4nNZNJrd8eGacXyklhj+aCpdhyqECugzZHahW9cEZ3b2yZ7Bo7tfBFxvZpJ3E+lRnm3viB4QNffHkTNsq8a
                        U/NtLqSUwue+LRhXno/MpuHOU7oU2ATidHd4ws7PVLuIWYASdic1jGGtURao33x3b8ZU89n2Ur8ISZKzZ45QFrtlnWntwLfjbVNWKy8hE6tuJGEQERKXZUFwOxflr5pROoY/bTiguCHgYA
                        QenzZipFeaNe073PAPOufef3pBAHfitm+RPl38+OrvQnhkceMmqwliAa8PNaxWjJeAsgS1uZlLnlSJ6ukc+X/llACkwjVuuK9plJYfMuR22hoBwqv/1fDIJdfeA1Ihfz1AYJk7vo38iQJJ
                        PtIqt7hKwPXzsXS9oLrRakMywr1rATIFHRdfAwhgpiQ0hqS8smc3X8YJ1TPc6/VFQC7MbCir7DEUxew0J/qReSIyAfM7oy+kaK2xFMLUPc5VgGBrPEtUzoSvmZQbV6uC/1UmyGwCukySuQ
                        bZscPJyXcTD/dFEZc8y77BRjFjQuKlFnKsCtI3TCunKBis8/Nr3f8YFIxucF63s9hLuV9hicfdDLgCt1Nw10BuKRrmDnktpEyHeAI+DtqCv9Xpj5CEjIWZ1+2lSBep72qtLsIuMWyHimdp
                        50nK3m3BRbpdp2UGHayfShg+x/KqdXBN2j8GhtZZIeW/ksQtX+AVR+0SM9y7Eu0ZrOZjbWL+opYXcTIau1aZymZs1ebSu0VK2K1wbftV3unGqKgarbbqYqKmFuB6IdwauUWNC4h/rg8uIA
                        gLvtPdKdY9D963uVpbSb7C/aKUvuHUgIY0O20uHuU8faSgS63f2S8qwSu9d/lAKRg5+UWyzwKwNf+Xk5Jwej9+KFDxOTmo7fcuiEzlPMDFLMU9D8pvrxxl3rZ7yPcj//ASuECmIyutojVY
                        kEXfbd/G6eWXtWgp/SqwK3QqShv/i4vp7C3p5SWH1m71ILFdq9pZNm7t819/w9oOlzO3HcAOQAAAABJRU5ErkJggg==' alt='Bot Profile' class='profile-pic'>
                        <span>BOT   </span>
                    </div>
                    <span>{response}</span> <!-- Display bot message text -->
                </div>
            """
            Element('userInput').element.value = ""

        Element('sendBtn').element.onclick = respond
           
    </py-script>