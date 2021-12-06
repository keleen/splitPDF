import urllib.request
import os


def download(img_url):
    basename = os.path.basename(img_url)
    file_name = 'image/{}'.format(basename)
    urllib.request.urlretrieve(img_url, filename=file_name)


arr = [

    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628489855004-aphvl3ift19.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628596321908-c29p7rguqdu.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628594775669-36ppwzzznjb.jpg',
    'https://mapapi.qq.com/jsapi_v2/2/4/142/theme/default/imgs/marker.png',
    'https://mapapi.qq.com/sdk/overseamap/logo/202107/tencent_color_logo.png',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628496823378-jy3994kg94e.jpg',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628498983980-nza7ykd214g.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628498971375-x7u649d6lzn.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628498958821-tgt1b6pkf6q.jpg',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628500075659-hqaf235wecf.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628499589032-dhckkbo9fc.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628499883830-j5j13wh7lsa.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628499801134-gzgbx449u9.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628499688125-k26jn4d4zqq.jpg',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628502179758-thum4upkt3d.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628502163459-53oql50uhb.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628502170490-ak5u0w9vk67.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628502079737-4y8cz8rboi2.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628501981562-vvacmvs5img.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628502033119-dtcmhjdmgs.jpg',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628587151630-8ot1uy22bmv.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628587070807-krsa0k1rp1.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628586951058-o7dhykudtre.jpg',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628587364503-zmfjglmnkl.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628587350676-x0y4m3q2i6i.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628587339912-vvy90ig8xv.jpg',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628587839330-5138b02sz7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628587854023-i7gd5rert4l.png',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628569145352-3lc5l27f5cj.jpg',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628575693475-a1umqu7g96.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628575786457-l59adit68br.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628575915105-2ao5znkw21y.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628575903728-qro6kbcvjsg.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628575832280-rvs0radrp1g.jpg',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628576201513-gk0sbeawqbo.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628576285634-b56wgdsc7t9.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628576471809-rw56r47ggbm.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628576401584-vmxttlvf2ch.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628576345068-tlqtsiawtfc.jpg',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628577507743-vvuxgiukhv.png',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628579740148-sk48fqogtf.png',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628580245977-suwotkc67x.png',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628580588235-pdusa55f0bo.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628580674663-vl6li1rgtoh.jpg',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628580640114-7kes26xxi0i.jpg',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628588195184-wokj5ssl5ke.png',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628581275742-6l467t7wg4b.jpg',
    'https://asset.eqh5.com/material/1625662292180-kiq146pts7.png',
    'https://asset.eqh5.com/material/ff8080814e957420014e95e1d66d01fa/1628582849137-94x8x4fq65i.jpg',
]

for item in arr:
    download(item)