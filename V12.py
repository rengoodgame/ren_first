
import urllib.request

if __name__ == '__main__':

    url = "http://www.renren.com/965187997/profile"
    headers ={
        "anonymid=jz5fvth34vncqj; depovince=BJ; _r01_=1; _de=AEA2E77BE42ED71F8B017DC724D2E63B6DEBB8C2103DE356; ln_uact=1518643602@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20110907/1610/h_main_PbMP_392b000013642f75.jpg; jebe_key=720835ff-331c-4412-ab41-4d0e402d1ea1%7C044908075707af5c27dfc8e5fbe61651%7C1565435572385%7C1%7C1565435573359; jebecookies=c6e8552c-6a60-4756-93d6-47d51740b1d7|||||; JSESSIONID=abc8WDUUnNxws81QHJfYw; ick_login=2e11522f-abe7-4406-a923-94a4994006f9; p=c7dc571d0c36cb88a7592de7795890f47; first_login_flag=1; t=fe5dfd0775d7c144aa6024bb86fec7b97; societyguester=fe5dfd0775d7c144aa6024bb86fec7b97; id=329720777; xnsid=7a719763; ver=7.0; loginfrom=null; wp_fold=0; jebe_key=720835ff-331c-4412-ab41-4d0e402d1ea1%7C044908075707af5c27dfc8e5fbe61651%7C1565435572385%7C1%7C1565608963368"
    }

    req = urllib.request.Request(url,headers=headers)

    rsp = urllib.request.urlopen(req)

    html = rsp.read().decode()

    with open("rsp.html","w") as f:
        f.write(html)

