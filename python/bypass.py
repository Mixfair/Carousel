import requests
import json
import urllib
import time
import asyncio
import aiohttp

# # anchorr = str(input("Anchor URL : "))
# anchorr = " https://www.recaptcha.net/recaptcha/api2/anchor?ar=1&k=6LeUPckbAAAAAIX0YxfqgiXvD3EOXSeuq0OpO8u_&co=aHR0cHM6Ly93d3cuYmluYW5jZS5jb206NDQz&hl=ru&v=_7Co1fh8iT2hcjvquYJ_3zSP&size=invisible&cb=9g4c77ga4vqf"
# anchorr = anchorr.strip()
# keysite = anchorr.split('k=')[1].split("&")[0]
# var_co = anchorr.split("co=")[1].split("&")[0]
# var_v = anchorr.split("v=")[1].split("&")[0]

# r1 = requests.get(anchorr).text

# token1 = r1.split('recaptcha-token" value="')[1].split('">')[0]

# print(token1)

# # var_chr = str(input("CHR ([xx, xx, xx]) : "))
# var_chr = "[84,59,27]"
# # var_vh = str(input("VH : "))
# var_vh = "494588590"
# # var_bg = str(input("BG : "))
# var_bg = "!aW-gb2oKAAQeDAeAbQEHDwKEwLOD81_50liTeY_3E0DCydeB96Q7cL96YYFIMnwt3L9rG_cQHEdz3g_9O9kvXV-0b9YifpCmMQPLrZ5TAY95Qfu3nMuOUjRgTmnpfwTOxsXFXYyEO3MQvYyH46HrFzngWRvVYfTCZuPtuxRjORknbrMb_RNOH7BeEjObDPlr4diYjCZMgLq8u8mrnv01jW8UVztUgRthtku7A67heI5wkzqUgAsJlZip-fUV47Ozb4f3oMcTiPyxhzBhD9C2HoCTNTSLvLqUhRSeb4qf8yql93M4YyXQE4iQ0pxEW9dERTE57cMtlzqjgE2dAn6rUh0iC98tyo6nl_0TyFOap2kbxMG7v4o7gtE4mKrUryf2qSZ7wSzKY9bbGFGIKKqf1OKNB5SCz819s5HB5NJbegYmzuTyCwkcVwU7qer5USkYSWqtIiUMif6YoFhzbbKIg8l-dROdDbydDMksEZpf3NrRKjr9usmLpx_QgYda9kG3zZR_EgjioxuzBDx-FFuAQZtXLeDyeJZgDKTCrgx0MELLANsGBbYiVsSOjjy5iuA7qsx7VCg4BtwVhxFpL9c36pTjvArBjjD8vol33XUD7JR7phE6ib2pcm26hqt0xWqDXtMkoJDYHWet9FZjPMS8PVJJF72EckuE0iTDAaJAh18gCBdsPu83xN4tILd3hZmwPgmJuP6hUkOdIz5i-bU8mf1pboEdwNV1nbf4k2zA0YYPHH78bdPyGcG7G9kseh5u2k39NMa6gkxG3gS_Zspzhj0pJAaFhXOzEeohlHmymstQxK4TrNIGgjgQ4KCYOZVfzqbGIJCT74n9q2lbYymERwPDO7SZxKEDLuNqNbhSkIN8rN6S78qcAC6Xghg_qaoznskaTvUI84MpqsbLUYrffGS2haj5pvV9Lak9ZNN7H9HB3nHN8Z5m*"
# # var_chr = str(urllib.parse.quote(var_chr))
# print("\n\nBypassing Recaptcha...")

# payload = {
#     "v":var_v,
#     "reason":"q",
#     "c":token1,
#     "k":keysite,
#     "co":var_co,
#     "hl":"en",
#     "size":"invisible",
#     "chr":var_chr,
#     "vh":var_vh,
#     "bg":var_bg
# }

# cookies = {
#     "_GRECAPTCHA" : "09ABBMTcNjd9XWZxYlndYKaaIl4Sar_4hKqHaue0SblbGjCx9sl9ZPw8T1MS0Bgj5X5MgzoN0HdlayEXypL-dOs74"
# }

# r2 = requests.post("https://www.google.com/recaptcha/api2/reload?k={}".format(keysite), data=payload, cookies=cookies)
# try:
#     print(r2.text)
#     token2 = str(r2.text.split('"rresp","')[1].split('"')[0])
# except:
#     token2 = 'null'

# if token2 == "null":
#     print("\nRecaptcha not vulnerable : \n\n"+str(r2.text))
# else:
#     print("\nRecaptcha Bypassed : \n\n"+str(token2))
#     # with open("bypassed.txt", "a") as file:
#     #     file.write("RECAPTCHA BYPASSED\n\n\n\nAnchor : "+str(anchorr)+"\n\n\nReload : https://www.google.com/recaptcha/api2/reload?k="+str(keysite)+f"\n\nPayload : v={var_v}&reason=q&c=<token>&k={keysite}&co={var_co}&hl=en&size=invisible&chr={var_chr}&vh={var_vh}&bg={var_bg}")
# #v=()&reason=q&c=<token>&k=()&co=()&hl=en&size=invisible&chr=()&vh=()&bg=()

# token2 = "03AGdBq27f4QEtZJw3pRuuS4vWyAexduhm8KVMIT--kjoPzDvlJbYMMoVers8RPkFcv9tyBglaa1UgYjqxrGucma0HmbEzChsviSTAeiY5GZ9jVYazEE8v8pAkf-qhkBddzTfWyWxUgaR7a3UmZWJqeqTlJaJgLl7DQNFjOArar2LT7UCplEG0G3owhNuYceOif2YFUMZBT-LC-f_XYU8vqRe2ry-5wkQNeOYNvcPIa6UlBkK0j6NWbYtH5dbi96HBo_-qRDnNehuiUwpzZ3UuRHCaiSTgN6z1i9V89z8uwWqbISVKiT1RBU5IV-QMlN292fchqGDMs7kRQBgQyUX1j9rOb4877__CFgcRdRssnM4cqgL3GHwSNRshlREkflPVjXOGDiHjHof90n5fmDDdqRFgQZsf93sp6CbkK3167Y8r-X3aEA4nWPqYRAmC9pRB-SMY0ywII6U4-iLStIRuXidX9JKE6JvS9FvmqBGgAil6DquBmc9vcQTKtYv1ffQMtAqMbgHiRBTAvnU0OmV9VGLnQqcTBGC_jY-1DKHczBePByBcSsR3emLL8ZNLjgG8fXLvEHKEQil6XjJbvLtV7Oj3dsPRFI1Lr2hyrzbJy8KaF-tgF265IYb6WlUMhiFW3oGe1s_emaFrBYDepJ_TdTMYvwjgiGCwaOPqv8z1FYPIWD6bSiHSLn4JRdvS0dd8bTDEXL6M_TpQl3qWzItKq_JC9eF0wK7WjfTkdPI9RNFHHC90mhFIN4KMzHiKGu4v8Lmv0Khx_KzCUbo1zBdMkf7QGCgF6Ipm9cx3HAnItknnUF1vqbDHLLXfk-jBaHurF1dywe44glgm2SNDboWVxKwYgHKPc1-IXCSkNGLsfxQgyzXYQvaMWE8X8NM689gUJVwVuP1H1V0dNpYHlG7uksMEW4H2x2iJxxKSWOF5ABFeoHHRwrhhjcmi0t7sAwl_-wxwFfE0iCY9ccf5-QeLB1GdIE0CPIPjzMVvgVWhg2dU7z96H_7RbnvuCtojBBb5UXoPTfgE32hhNcmrjx-F8bS7Zp-4SRj_uCDa3bXj782tMB7pPcZnNt2eKp6GVYlzOEl7evCX6n9obpkeRN5NdiA58QoGZrU5DOKEdnRIuYtxGy7OvOBzE01Ah1F5QAsxXzfOwkUsqOcfTAn0RSl4Xfmg73ZrKOcE9AkhsUoedgOGe0BkqRBwvKvYYN-B09p7euhscvaQ-xbJLf1ux0aS5oIt6n3cLw5ZIeuObf4Q1B000bbHpf5Z1Ok"

# http_proxy = "http://18.141.11.227:3128"

# proxyDict = { 
#               "http" : http_proxy
#             }

# r = requests.get(url, headers=headers, proxies=proxyDict)

# url = 'https://www.binance.com/bapi/nft/v1/private/nft/mystery-box/purchase'
# body = {"number":"1","productId":"163164431084832768"}
# headers = {
#     "accept" : "*/*",
#     "content-type" : "application/json",
#     "accept-encoding" : "gzip, deflate, br",
#     "accept-language" : "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#     "bnc-uuid" : "f404df40-b4d6-4200-a6fd-d026f5dccfbf",
#     "clienttype" : "web",
#     "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
#     "origin" : "https://www.binance.com",
#     "referer" : "https://www.binance.com/ru/nft/mystery-box/detail?number=1&productId=163164431084832768",
#     "fvideo-id" : "3203d115c760a9979a5148e7cb4723b02206042e",
#     "lang" : "en",
#     "cookie" : """cid=Q2mKEfy0; __BINANCE_USER_DEVICE_ID__={"2a7c60dc2df1c58ecd6cf5e2f4b16453":{"date":1638832745779,"value":"1638832746001hSZcvl82AtMhF0ry3aw"}}; home-ui-ab=A; bnc-uuid=f404df40-b4d6-4200-a6fd-d026f5dccfbf; source=referral; campaign=accounts.binance.com; sajssdk_2015_cross_new_user=1; _ga=GA1.2.2086413799.1638901306; _gid=GA1.2.1600667209.1638901306; BNC_FV_KEY_EXPIRE=1638987707015; BNC_FV_KEY=3203d115c760a9979a5148e7cb4723b02206042e; s9r1=B0A0BF55088E01AA33865E192E211E8F; cr00=81F1982FBDD2D6C79349772845D97447; d1og=web.358744785.7579F7F93BA78C365E55F04ABF67333F; r2o1=web.358744785.DEF1BBEA35E1E3803D8A696E76E01780; f30l=web.358744785.A542322470DF6598F0BCA2FEC04586F1; logined=y; isAccountsLoggedIn=y; p20t=web.358744785.35B6821CD474453799818E379197864C; fiat-prefer-currency=RUB; nft-init-compliance=true; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22358744785%22%2C%22first_id%22%3A%2217d9621538fb90-0857712d5801a5-978183a-3686400-17d9621539011b6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217d9621538fb90-0857712d5801a5-978183a-3686400-17d9621539011b6%22%7D; theme=light; lang=ru; userPreferredCurrency=USD_USD; _gat=1; _gat_UA-162512367-1=1""",
#     "csrftoken" : "0f74ff85a2ae2f8a30e47f187626860c",
#     "device-info" : "eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjI1NjAsMTQ0MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjI1NjAsMTQwMCIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoicnUtUlUiLCJ0aW1lem9uZSI6IkdNVCszIiwidGltZXpvbmVPZmZzZXQiOi0xODAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTYuMC40NjY0LjQ1IFNhZmFyaS81MzcuMzYiLCJsaXN0X3BsdWdpbiI6IlBERiBWaWV3ZXIsQ2hyb21lIFBERiBWaWV3ZXIsQ2hyb21pdW0gUERGIFZpZXdlcixNaWNyb3NvZnQgRWRnZSBQREYgVmlld2VyLFdlYktpdCBidWlsdC1pbiBQREYiLCJjYW52YXNfY29kZSI6ImE0MGRkYTMyIiwid2ViZ2xfdmVuZG9yIjoiR29vZ2xlIEluYy4gKE5WSURJQSkiLCJ3ZWJnbF9yZW5kZXJlciI6IkFOR0xFIChOVklESUEsIE5WSURJQSBHZUZvcmNlIFJUWCAzMDgwIERpcmVjdDNEMTEgdnNfNV8wIHBzXzVfMCwgRDNEMTEtMzAuMC4xNC45NjQ5KSIsImF1ZGlvIjoiMTI0LjA0MzQ3NTI3NTE2MDc0IiwicGxhdGZvcm0iOiJXaW4zMiIsIndlYl90aW1lem9uZSI6IkV1cm9wZS9Nb3Njb3ciLCJkZXZpY2VfbmFtZSI6IkNocm9tZSBWOTYuMC40NjY0LjQ1IChXaW5kb3dzKSIsImZpbmdlcnByaW50IjoiNzY1Nzg2ODhlZDFkNTY5NGQ0YTFjMjM4YWNmNWEyMjQiLCJkZXZpY2VfaWQiOiIiLCJyZWxhdGVkX2RldmljZV9pZHMiOiIxNjM4ODMyNzQ2MDAxaFNaY3ZsODJBdE1oRjByeTNhdyJ9",
#     "x-nft-checkbot-sitekey" : "6LeUPckbAAAAAIX0YxfqgiXvD3EOXSeuq0OpO8u_",
#     "x-nft-checkbot-token" : str(token2),
#     'x-trace-id': '053f02dc-dd63-4911-9bbf-17da8529160c',
#     'x-ui-request-trace': '053f02dc-dd63-4911-9bbf-17da8529160c'
#     }

url = 'https://www.binance.com/bapi/nft/v1/private/nft/mystery-box/purchase'
body = {"number":"1","productId":"164982370297592832"}

with open("/tmp/headers.json", "r") as read_file:
    headers = json.load(read_file)

print(json.dumps(headers, indent=2, sort_keys=True))


# r = requests.post(url, data=json.dumps(body), headers=headers)

# print(r.request.url)
# print(r.request.body)
# print(r.request.headers)

# print(r.content)
results = []

requestsNumber = 2
saleTime =1638839945-0.5

def get_tasks(session):
    tasks = []
    

    for i in range(0,requestsNumber):
        tasks.append(asyncio.create_task(session.post(url, data = json.dumps(body), ssl=False)))

    # tasks.extend([asyncio.create_task(session.post(url, data = json.dumps(js), ssl=False))] * 100)
    print(len(tasks))
    return tasks


async def get_symbols(headers):
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = get_tasks(session)
        print(time.time())
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.text())


def startSsc(headers):
    asyncio.get_event_loop().run_until_complete(get_symbols(headers))

# while True:
#     ts = time.time()
#     if saleTime>ts:
#         print(f'{saleTime-ts} - осталось секунд')
#     if saleTime<ts:
#         startSsc(headers)
#         break

startSsc(headers)

time.sleep(2)

for r in results:
    if len(r)>250:
        print('blocked')
    else:
        print(r)

# token2 = "03AGdBq24IcK3paYATbehyrQtzu0WCnxi-5BVk3Y62sOKFAHXm9IlMRkB2M31O7EA3kVfBFCMdue0Z4repmADCxxVEk1hvC7rf5n6vmwI2g1cErWk_VcFHSWtI6r8SWta0RJAdBisNMtgNm_fsJwE4_gmUoYQllMUIzB-j_a2k3ieGuy2YcYQRre3tom-jH7B90g-kUvDTGi7ZCfZVqhvLqZ8PwfBe0go05UKFNbwu92HqOC1d4Kz4i56tArBlWi57s9mQ62c2cMWjNhwpsIMgfzyR-u3TMS5A5ZRrilWJBX1RVBIYQuHjV8ksxZn5Riw7lr3sGmUD3CHclmEfZdHwiKAO2DwzCuJMTqRuuaDS43Le68pYyzizcOiC72PfUjpeTy7jBEy6BuoojesddZfubpyssJ_JDEBim3nWylNzcL-aZKg2KcqBXI3zPb6fl-kb5nzD0QNrFGxSiL-dtMBpaNIRrsbvF04nHCamH2fxJCA6N9PyUHKIwF1JLozgn-E79pnzzAyiFEnpBgr4Tasli55mEfP2fEhkPURidvVDA6U0HEdSgDmtz_naBV6jJu_ad_QdR-bRjfT5ehSuPw23CnFE24PSJAbBRvK_vSWjqaptZ8p4DaujoOeyLMHHeBaBNreQuTiUVQxS4QwsLpVblxkaUDqijKOHYVUioiaTshOcUS2B51qLuRFwucArAP90g8itN7T2K8Q-6OZ8xI3EyBRu6ZdAkIxVdIEmqB9ypTbNYf2qZ9wHFY95TPmzP5pycQrwOEq25mFQJgWCB9Nqyp4do1PWXeVNDbZvPjwPG9rK-YTz5KoWwrRkvD1trLXAKgsneEBqWJnMQFucHsuizFg8MWxVqsHzPYD7eVKow5NpL7uQnohbvZJMJnPSw5uRqjDQ7B5-ujqsIvaiIyETQLemGkP5hnLF_yLL3x0uoId17UaG6y1ZkTTR9M9hPxHYxR7-_YaMAstEjkPWNGgVD-2aX-ZnGoQhUEEG5pVflx9XdOrTrAOqBDJRWE13w5r7Aezct_DFaD7aRQ5OY1wPGxUfhxqEXUAhskVwQ98UpJ_1wlGyV5Jea-GAL00I-iWnPBgEyEY7AG2E2dbVkzKS8SnXhZAVVW4IwWTFPpQH9wdjWuQ1PZtoeCwCeQe5MZIsSZELBL3auaAQw8CxlUttMmv5DBWXcmtwz0WPycd3M6KV0froCl_wHMVLzRWQ3LuHsoasofQiEdUgHXH9C7yms0ZVshqTX0Y10jaRkg-D370r0y5aAo5rro-JfnxiJ9dHnESEhgwn9hbAahsn6EXiVquS_WTNrSwU_5qcCwLnAsdRocuFyOnn3JFrWDCuECS6c--mA9bTP1ovOQQo4_Bj043hOedzeLVu1pzEnLBLEdctVpzeUz_oTSKaEx8Q3FzgADmgvVmN1d17I0avXMEtortEkGnEevBnULRwVrnDJqosAdpuXzWfmxlR0iLdFq0KMHmkDW1meFpGxQC3a9QfQiPp-SW49Fvt_w"

# url = 'https://www.binance.com/bapi/nft/v1/private/nft/nft-trade/order-create'
# body = {"amount":"50","productId":14441741,"tradeType":0}
# headers = {
#     "accept" : "*/*",
#     "content-type" : "application/json",
#     "accept-encoding" : "gzip, deflate, br",
#     "accept-language" : "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#     "bnc-uuid" : "3dcba473-0c1e-467d-b94b-63eacd38fbdc",
#     "clienttype" : "web",
#     "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
#     "origin" : "https://www.binance.com",
#     "referer" : "https://www.binance.com/ru/nft/mystery-box/detail?number=5&productId=161811045018105856",
#     "fvideo-id" : "3215706665c6ab809b525cbbf776cba02ecc90e4",
#     "lang" : "ru",
#     "cookie" : "cid=MjlNSii8; bnc-uuid=ab036a17-278d-4f9a-ab18-4723fa95d7ab; source=referral; campaign=www.binance.com; _ga=GA1.2.887501590.1638371919; _gid=GA1.2.598102021.1638371919; userPreferredCurrency=RUB_USD; BNC_FV_KEY=3215706665c6ab809b525cbbf776cba02ecc90e4; BNC_FV_KEY_EXPIRE=1638458319535; nft-init-compliance=true; lang=ru; gtId=3a28a2d8-1728-451b-8046-ea0c7aab2a62; cr00=0505200480BA1FEBCD6539866515C6C2; d1og=web.131767133.B5C8C033055BCE646B67802499EA316D; r2o1=web.131767133.112FADCC2EB1DB9F42C86BC2AF03DAFC; f30l=web.131767133.F7DA0318319D8630EFBE845D2D03C1DB; logined=y; p20t=web.131767133.851DAD65AFE97DD4A24129CB6E68F849; home-ui-ab=B; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d7693855f179-055e06fd0b4a43-978183a-3686400-17d7693856011fc%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217d7693855f179-055e06fd0b4a43-978183a-3686400-17d7693856011fc%22%7D; fiat-prefer-currency=CNY; _gat=1; _gat_UA-162512367-1=1",
#     "csrftoken" : "03f6456b90b9525dbab41326e4a38f26",
#     "device-info" : "eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjI1NjAsMTQ0MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjI1NjAsMTQwMCIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoicnUtUlUiLCJ0aW1lem9uZSI6IkdNVCszIiwidGltZXpvbmVPZmZzZXQiOi0xODAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTYuMC40NjY0LjQ1IFNhZmFyaS81MzcuMzYiLCJsaXN0X3BsdWdpbiI6IlBERiBWaWV3ZXIsQ2hyb21lIFBERiBWaWV3ZXIsQ2hyb21pdW0gUERGIFZpZXdlcixNaWNyb3NvZnQgRWRnZSBQREYgVmlld2VyLFdlYktpdCBidWlsdC1pbiBQREYiLCJjYW52YXNfY29kZSI6ImE0MGRkYTMyIiwid2ViZ2xfdmVuZG9yIjoiR29vZ2xlIEluYy4gKE5WSURJQSkiLCJ3ZWJnbF9yZW5kZXJlciI6IkFOR0xFIChOVklESUEsIE5WSURJQSBHZUZvcmNlIFJUWCAzMDgwIERpcmVjdDNEMTEgdnNfNV8wIHBzXzVfMCwgRDNEMTEtMzAuMC4xNC45NjQ5KSIsImF1ZGlvIjoiMTI0LjA0MzQ3NTI3NTE2MDc0IiwicGxhdGZvcm0iOiJXaW4zMiIsIndlYl90aW1lem9uZSI6IkV1cm9wZS9Nb3Njb3ciLCJkZXZpY2VfbmFtZSI6IkNocm9tZSBWOTYuMC40NjY0LjQ1IChXaW5kb3dzKSIsImZpbmdlcnByaW50IjoiNzY1Nzg2ODhlZDFkNTY5NGQ0YTFjMjM4YWNmNWEyMjQiLCJkZXZpY2VfaWQiOiIiLCJyZWxhdGVkX2RldmljZV9pZHMiOiIifQ==",
#     "x-nft-checkbot-sitekey" : "6LeUPckbAAAAAIX0YxfqgiXvD3EOXSeuq0OpO8u_",
#     "x-nft-checkbot-token" : str(token2)
#     }

# r = requests.post(url, data=json.dumps(body), headers=headers)

# print(r.request.url)
# print(r.request.body)
# print(r.request.headers)

# print(r.content)


