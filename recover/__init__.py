import check50
import check50.c

HASHES = [
    "6e2e4e56677e55cda750a2c0bc1c96fb4952ee37aafcc0810d0d5a883834abee",  # 000.jpg
    "4b9e49c8b47574ecda37045f9a8411f5cdc02c767cbe0d021d158321f730c26a",  # 001.jpg
    "990a411e113591709fa89a328eb8e436d91d68f5f1b1a546af24420cde661f61",  # 002.jpg
    "d6d8d48565cf57c6e7ddf14e21e40bf546d25353acac0cc026f9531972851ff2",  # 003.jpg
    "288d010963df4e96c77ce7f3ffc0f6bd46c27ac2cc9adb727b45c0b87ab275fa",  # 004.jpg
    "c1fa2d60b4706adb349d26c6a09c576ac067a26ee2567575212c76db196f2890",  # 005.jpg
    "c0668071c0725b703292388f89ac73ef18d2d3c52675d896f8cac9044c0b4988",  # 006.jpg
    "39f39df0a38bb40613ae906bf6d553960fa03e4ed0869a8a16037a212d2b183c",  # 007.jpg
    "ec4f9fce24c6f289df0bad61cc211ef728c35d334b44e20163d54037e290c160",  # 008.jpg
    "b11d27826c4048dd053618d702ecb23171678e773a75cee6edd6312670ed0eb8",  # 009.jpg
    "67e790bad94ac0f701f337df1519548d8afdf44b22a68c833dff3f76de6e364e",  # 010.jpg
    "966806bba9a8a49fd1451ea03790204cc08ba0bcb637c962a93727615f025c87",  # 011.jpg
    "ae4e8f59f84e9aa0ca702ce6b8620be0565cbbc55dec8aaf92af2f606044e123",  # 012.jpg
    "bafe56cd662f886829a49230d950f287ad583029da2431ae8788994aeb549aab",  # 013.jpg
    "44c60f88c061aa6008394f4301aee097fc870fe2ae3a22c7e39edef408439f16",  # 014.jpg
    "2f21b7b99cd7153dd4b97505453ce87e33161a53e97e1b1bada3aff2dc774728",  # 015.jpg
    "30078deaa315d274227eff3e8e3f730cdcd4e06f971d1d4a44d3f5a8c3edbc04",  # 016.jpg
    "9c09aad678e7bc82eab00728dcfa38cf8d52de25e1bfeb083f2db5ab1b8f3786",  # 017.jpg
    "f99e1f38af9ce6a50f6f11c70e1c865688eb69fd9afe12fb9a0bf1ce40e3c9ab",  # 018.jpg
    "c0776497110093f0d70197b728b3cf37e55bbffb6f49c6a3e9f2c5a46c42975a",  # 019.jpg
    "4c03feed830d68545b7f6837db995b7bbfad33555580e0e831204e8c591e0c4f",  # 020.jpg
    "81af2f47dc25e1397684c1bf0fd9225034684dd6da42240cbe0a3c345c08678a",  # 021.jpg
    "7a67f5661550ebd79663be561d4e420038f05b4c2e8306416fb5030249c57f47",  # 022.jpg
    "84407f55d629fbf81c25484e412f63174638db2cafcec74e78cca01c5134f2fa",  # 023.jpg
    "92d715f3e6553403b3f9b68570ea0ed3bd89db0b99c5d8cbde8c25f2c733f0cd",  # 024.jpg
    "96299930a11513ca8ffe4b3426f957ccf68d7c84772ba752c2aa0ead6f117ce4",  # 025.jpg
    "78dad5106fcd1052ceefd1c013cc544c090d664da07ce1025e28a789d140be8d",  # 026.jpg
    "539e6b485288338bd0ace9cef311fb6bc5efd3ffb0d769721002e8a1a2eb68b7",  # 027.jpg
    "d656dab59345af3fb9df34ce5a31886fe3c4d2633266ec96ae57201c1aa18e43",  # 028.jpg
    "3ac42ce7b40dde22ae5ac5c1b69c9cd58158b46cf5f3a14e52c74257f51c8f51",  # 029.jpg
    "9bd0e716f213dfe1ed3c2c1a8a4077104f9388a0af64bcc07da6906f95775700",  # 030.jpg
    "b6ffeeaf60e6bc6bf733ca83db10ec17e58af10316e63beba3e61f33a6f8db84",  # 031.jpg
    "7781c4bb34779896ff1c26889016cdff97ad60e1a22f4ec83e0ca36784f4e651",  # 032.jpg
    "3333366e997dec367a1a2322bb660b50a7940c466327dd3dc00d799a2e92c428",  # 033.jpg
    "836e10d85ffd2cc14c34e9218eed216a752a68bd5cf0b322cae22171339a9cdd",  # 034.jpg
    "da7cc764f91010403b4f416483fc970e08116fdcbabb504ff79a67299219f3c1",  # 035.jpg
    "92b8c2a16359de4b82e976309d0e7838d56a7a4fb5ff4bd6f2625f6b7805b13c",  # 036.jpg
    "0f50bc6acf71d9dc5b4b15aec006d8465f6d1f46b0a787e8420d30e7dd85626c",  # 037.jpg
    "1bf7c6799cb74f2cb057e3cb0efe56a7777e653e4d17d1780e2360b4dea8d47a",  # 038.jpg
    "4502eee8af402ee60f1960e900cc424bb146799b0a301e93ab9746cfa260b90d",  # 039.jpg
    "4c149d5a4e10fd3dd1895e488d069c3ce25c18266a6807e7510bd4eb0fdbe482",  # 040.jpg
    "b5a1e39de5116132cf953faea6c74f7a154299eba20a03c13574919df5b2dd38",  # 041.jpg
    "b6e9765fb868149f4b92cfd2105bc84fb9207548833c3b7acfdc7c32adb1b4c2",  # 042.jpg
    "a975555bc31d92fef13889d2c87f91ff01ab5378e429634fbd12f3934d55ba6e",  # 043.jpg
    "2dc63155d61c705f9047f5349f46397b03aaa7b9180e78b27fd4b00d698cec95",  # 044.jpg
    "ed6d5984b6fd0c2b91cc5adaf7b595757281452fe78158f4dcad01d2c4fe03c7",  # 045.jpg
    "b2163d1377423727e6fd603ee6b20383bf90a742fc854be12783faa94129a6b3",  # 046.jpg
    "c08f342831bc36a9f4cccc2312876ce0abe785a77d579dfb2eff0c6fe1d71b6b",  # 047.jpg
    "bba63b6b98e0b5c6fbba24fd840a8eac0ff2b86973338e89ef699920c8835e30",  # 048.jpg
    "0ff470f2272f656483779e1901611d9c5237df521e51b5aab80760c5c95689af"   # 049.jpg
]

@check50.check()
def exists():
    """recover.c exists."""
    check50.include("card.raw")
    check50.exists("recover.c")

@check50.check(exists)
def compiles():
    """recover.c compiles."""
    check50.c.compile("recover.c", lcs50=True)

@check50.check(compiles)
def test_noimage():
    """handles lack of forensic image"""
    check50.run("./recover").exit(1)

@check50.check(compiles)
def first_image():
    """recovers 000.jpg correctly"""
    check50.run("./recover card.raw").exit(0, timeout=10)
    if check50.hash("000.jpg") != HASHES[0]:
        raise check50.Failure("recovered image does not match")

@check50.check(compiles)
def middle_images():
    """recovers middle images correctly"""
    check50.run("./recover card.raw").exit(0, timeout=10)
    for i, hash in enumerate(HASHES[1:-1], 1):
        if hash != check50.hash("{:03d}.jpg".format(i)):
            raise check50.Failure("recovered image does not match")

@check50.check(compiles)
def last_image():
    """recovers 049.jpg correctly"""
    check50.run("./recover card.raw").exit(0, timeout=10)
    if check50.hash("049.jpg") != HASHES[-1]:
        raise check50.Failure("recovered image does not match")
  
@check50.check(last_image)
def memory():
    """program is free of memory errors"""
    code = check50.c.valgrind("./recover card.raw").exit(timeout=10)
    if code != 0:
        raise check50.Failure("valgrind returned a segfault")

