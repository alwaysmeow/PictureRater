import requests
from bs4 import BeautifulSoup
import json
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Cookie': 'yandexuid=7689425991692039709; L=WF92SlFnbgNgYlt2S2picwdGAH5/BF1VCkAaKS8IDhIQQg==.1692040329.15434.320126.fdd2d1834c0a1e26cf86509fe4c80a10; gdpr=0; yuidss=7689425991692039709; mda_exp_enabled=1; mykpFolderFormat=full; mykpFolderSort=default; mykpFolderOrder=asc; mykp_button=movies; my_perpages=%5B%5D; location=1; coockoos=4; hideBlocks=1536; yashr=1915476411710839363; _ym_uid=1696266589999367049; crookie=Y9ELFXz1nAMduePnJEPLylqg8W9URfMOuuroYPhDuAV3tqleJOGm9mKFcFeuBbKIel2mKH8gitcPPLNdCADwL1z/W9s=; cmtchd=MTcxMjQ0MzE5NDI5Nw==; mobile=no; _csrf=VAJ0WF3SgVF0i7qpDluOeBZ4; disable_server_sso_redirect=1; _yasc=wbtW3BQkC9hmBECM2kEtEmfjVDBn8aJ0XfkDMePyfOmErrHEenW9jIy7zn2js8t2nw==; i=e160CADtgydCcZXdmtzIQrTyMlhK8812SFj+ut3iw/mjf2mDRuDEsj9kNdmk2WlMnEaLBBmYAo8jOB05Jn3/r2mJKYs=; sso_status=sso.passport.yandex.ru:synchronized; no-re-reg-required=1; _ym_isad=1; desktop_session_key=764710cff3ad798e274f3cf80f882b31e3524df69130b0fcadf5cd3f785b32fe0e437bd002f495747884574b6fd20ff0c7338c5d5b57d79acb77c0845c881a45aaa95f1ea922d5c3f5d3b2be4829e0e06c79036d96929047d26193075ac76a1c; desktop_session_key.sig=9q3te9C-c1jUH3kyQXHnVvqBboE; yp=1712765016.yu.7689425991692039709; ymex=1715270616.oyu.7689425991692039709; PHPSESSID=fb04d9ce752e2bda7968229238b2fe7b; user_country=ru; yandex_gid=10740; tc=6121; uid=39950340; _ym_visorc=b; yandex_login=; ya_sess_id=noauth:1712679759; sessar=1.1188.CiDnRsMDGgP3F2P1uv_2d9Xnt59PU101AkuROeuLo50ndw.vCLSlHLbY1VbNhc-WrEtrJX9G2uiu8NZgX4w4VvmjUk; ys=udn.cDpjNGxta2VlcGVy#c_chck.4112252683; mda2_beacon=1712679759137; _ym_d=1712680396'
    }

path = "kinopoisk"
blocked = False

def parse(id):
    response = requests.get(f"https://www.kinopoisk.ru/name/{id}/", headers=headers)
    print(f"id = {id}: status = {response.status_code}")
    if response.status_code != 200:
        blocked = True
        print(f"You're blocked by website. Ending.\n")
    else:
        soup = BeautifulSoup(response.text, "lxml")

        tag = soup.select_one("#__next script")
        data = json.loads(tag.text)
        try:
            gender = data["gender"].split('/')[-1]
        except:
            print("Can't get gender\n")
            return
        if gender == "Female":
            img = soup.select_one("body img.image")
            try:
                img = requests.get(f"https:{img['src']}", headers=headers)
            except:
                print("Can't load image\n")
                return
            with open(f"{path}/{id}.jpeg", "wb") as file:
                file.write(img.content)
            print(f"{path}/{id}.jpeg created\n")
        else:
            print("Gender is not female\n")

start = 104
end = 4000

for i in range(start, end):
    if blocked:
        break
    parse(i)
    sleep(0.5)