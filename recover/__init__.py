import check50
import check50.c

# Every other hash is for corresponding .jpg without trailing 0's
HASHES = [
    "af5d4d3920480f85d4c47be9fd538f5dfbf4937fd7f1153fa9aa2e5c96963707",  # 000.jpg
    "45b5cc2f6ab4548d9a2619e53cddd5f146fdd1bdf37bc83a2bf0b12392ef0b41",  # 000.jpg
    "6996fb386f8f97d5352fad805d3adf0d4f2285bd7da7f0081050876b6f144974",  # 001.jpg
    "e6038ea8cd73251bba72f2b3a7b9378e90d41683db0913586f3f69418dcd95cc",  # 001.jpg
    "e7b2b4d3e7dcef5d3bc432ec899b7aca6486078dedaf5fd3b6a4861f1fe884c8",  # 002.jpg
    "b225157aa814f30aaa6fa0d704b4153a6147836ff5170595379ddb50410e3fb1",  # 002.jpg
    "91e9144adb34550447fe68ab6603db32a52bf7226eb7257132a55f0446f5d436",  # 003.jpg
    "97f7b54cb23540a915213054c604bc8711d22343f3b43089217580f302d0bc4d",  # 003.jpg
    "ff14332d8916081d76895facf964e2605a8218973abee9ddfddf375630fa6464",  # 004.jpg
    "3cb8a4f6a8c7f91ea7fc2d46d21d657ed06143e0920533c206ded9e1b15f8b6f",  # 004.jpg
    "db66fdb0353e1a1cc72117d1fd2105aa85185533dd8f9255c949bb32b2151cfb",  # 005.jpg
    "d654c9d400bafde82b9080eaf43d58e7b4b4f701f1a79ce59c82f38fc4779427",  # 005.jpg
    "64d38d7b239bb33b15e1f6c98759e455e68124b325dec581cc14d64efeeea2d3",  # 006.jpg
    "97f6bbf8b80bf770509bd28712caeabbe6ffeca1d98acbf7bf52ebc95d671a84",  # 006.jpg
    "ea4190741a9ffc66fe1c54e17cbfed8f4faa9a16a3a328004aabe3f0a7e23758",  # 007.jpg
    "614432fcaf3e5f4a21116f3d353b2440a96bfbe1b11833cfd30b37baac161a1c",  # 007.jpg
    "dbc61a1d664bb585f911eb4852c66f49e247865137b097a7718cc2c8a8ab48ea",  # 008.jpg
    "11225b072faea9497149cee81cb1bd7de7ea7254fc7f0bcf33569da54780a4c2",  # 008.jpg
    "67a81febb0d0dbe5fd0a61f53fea1925c02be898855bda714dda3bc101ecff89",  # 009.jpg
    "0a0f9e458016163c2bfd7ed88735f1819f2e10d7b7df6491a66373fdf55a4527",  # 009.jpg
    "775118ca83bac649d16c268fbf47c8950b72e9b0d8ce56cbc73c28f4797af9c6",  # 010.jpg
    "2e3f67bc9c65505621a7e4e33f74699bfc8c8fc20cd8dd6676d61e07e856c849",  # 010.jpg
    "a0699810661598281d0788dc508b7c5c3e3cd8f45d293adbd96c0fce3bb7e06e",  # 011.jpg
    "00d2f0fe6fd96059b9077bff1615528aa32998321014fb3c0f4b25f9c5c4cc28",  # 011.jpg
    "0018682f939c81dc82f9a84368f433bc25feb4e09f160cce0facbf33b95e32ec",  # 012.jpg
    "d6703aacf581f213632008f9f3115e0672025015413c782c24ee0c4359ea9e21",  # 012.jpg
    "d1dbd92fb666611b8d4419ee72e63f4ddb009f6e7807d4512ee3be4283030f21",  # 013.jpg
    "163e5a81298d3cb7f79d2f24a79f94435c4cc70c535ac42866e9343d7711a89e",  # 013.jpg
    "878066b209e4bcb97c806b410a7930c018bcdd32245014e43f664fb54d8374fb",  # 014.jpg
    "2ce9a9ab03dee04cd08496cd6472c9527355f840076303177d7a9dd3ebb22149",  # 014.jpg
    "5e7213eb03f07db1b39cdc266f52727c7f8e7102d66191292619c473c9bdd393",  # 015.jpg
    "24f3ba12467c2163e708316e43909aa6a65f35cb04b3ec9983126a0c154f8916",  # 015.jpg
    "935b53246c28ca94ce90cd3d01e104d79e73797a9eeb4b16a6f930e6b535b461",  # 016.jpg
    "2c31334b18d21419fc87f74f20bc9f1459e731ad03a0b59b997194524daec722",  # 016.jpg
    "e5b740b53f3b0e410308128b4c5bfb2930da0ff11fa1a8386a0fbd15476bd131",  # 017.jpg
    "bcb1846cc6dff5b4487c81dea28489ebce618fd0d4f04927771f33bdd96a1d3e",  # 017.jpg
    "0bfd055454bca8798b4eff6dd0f57abc23c653a31d6d310104b82413596fece3",  # 018.jpg
    "b702ce57f158d3fc04e79fa18a8b98071b1c3f5d07dc66fa1b12061de4b9dd4d",  # 018.jpg
    "4936141707bfae8d3d0080e0b16584dd65e260994727c8a8f33f1ffc242f433f",  # 019.jpg
    "a68e38ac3a106c7d74d6096ad4be890aea5a97a77e9fdb4b20c8cc5e9ffb8967",  # 019.jpg
    "3c5c37a5aa32386f527a060066f5812f37f6aef4d178191f1392e03db7f3fad0",  # 020.jpg
    "84dfd960155cc57daaa3ba3d40c628942fe9bb353ef1064ef1ef1aa159f2736b",  # 020.jpg
    "c596292224bf4e8b1cfc32a1649d1e0ee45cf563d35dffcc5d9819227efca992",  # 021.jpg
    "7fd78eba897fcaeb90d8968af2a46a399a3a9b5c44c54933ac50b4d8f30b9042",  # 021.jpg
    "14ffd5ceede9a21bd18a50c7fe474f81a9c07fadba845ba21fb7d2ddaf87dca6",  # 022.jpg
    "6e918407ddebc8e7f39451c1a69dbe71a9a8167da3dcc2b840a7c6fcb08b2306",  # 022.jpg
    "7926d6654651964167561f9be2af5f417b1160598395f17d74e25540396b072e",  # 023.jpg
    "a9033f4086c83d55e9fbee500dd9eba715c51848cfa1c91b97307600df2940d0",  # 023.jpg
    "509f7233a90d1e50f0c01dc51c4f82df50ccb3e87b74801b414e36b3025219d5",  # 024.jpg
    "081e83a063936742cda5515e13513d93984c7752c713f729a9544c2aff5ce7f9",  # 024.jpg
    "8ee5f5115b73aed853341c5cfe275d62d102de549c1cb1dd7aa2952ff9399c72",  # 025.jpg
    "19e590717522316983d83b25bcb69eba29b7a3c068ac203c5aa2206b6a6f5bdc",  # 025.jpg
    "9eba5b4bd473350f8a0ae2499782db240d97f995d0af16797f6356ac947eb7fb",  # 026.jpg
    "53fe31d321cb46320e3d6ce51c62cb79e74f10f990f23a2e96d4484cbe537981",  # 026.jpg
    "118d5bc8da0ee8e8b9eddddf94c76b2824c2d0eacc63b4da895446d301e288c6",  # 027.jpg
    "122e3c1f6a31accc49d0c5129585bbc524963d1299a57aa1c8c90694d91efb7c",  # 027.jpg
    "8c367af67f100fe7711f1aef2cd6540e39d55a058fb7c5d021346fb03df2093e",  # 028.jpg
    "918276cc5093db1ed8c160d1280393859548ba977834867add59f5190d168746",  # 028.jpg
    "0ac44b8fd5f2033f47789bd5508a6640145b00cda625a4e47ad687e8b26e49e5",  # 029.jpg
    "317c9c87610b4cef3b1292d15869ce54eed4405b6d19d8424b0829f4daadf0dd",  # 029.jpg
    "8401afea4b369a1162fba88e1ba575eeda9dbf8d32e89f65aba5e16a336af9e7",  # 030.jpg
    "60c49934481b76471e844c299d1628bbae00b647c5bd37d33dedaf03c0c02cba",  # 030.jpg
    "374c2a1cb2059243d895fd5b4cca32a81b39d89560081695e700b1b5a09fd8d9",  # 031.jpg
    "b9ac6d258aa145839991e869e9bc261071083af3af5f33c1ee9509fe4e855362",  # 031.jpg
    "d0bebb1d70b878c6d21fb93eddb249f953f025dfb1220fcf8859fc9c0af2e810",  # 032.jpg
    "d585a629d69772b86ae5b17a0f423cf75dfc6ee28858d1d59f034857388f013e",  # 032.jpg
    "c769f6b0671024cbe5cd6faffceb74394dfe008443a28f27c1b241f843062e0d",  # 033.jpg
    "6cd9b6c4c0620bc37a95a86770824e63ffaaf492aad784b008bbc52b40606f75",  # 033.jpg
    "2ed1081072bf80ce9ad70b32a14dbfd7f3a1d9b44d5bf4ad8afecceaa0b339fd",  # 034.jpg
    "f46387e778c0d0c756288742e8d30a978eeace3c75c50c84a8cd717083f8dbf6",  # 034.jpg
    "22aa5c24c5ad996e90206ce6ae30831664b72da54913f3f605b230fb38c8ba72",  # 035.jpg
    "87a844eef028094ae1c3d115ff0a6b669049b8f7c92499f99ca75cdfc96bbb4a",  # 035.jpg
    "c1fbf91e81d6415173877b1e46eb1c42ac42ceef3f8ff25ce6df5513aed857e2",  # 036.jpg
    "03d9cd718e1b1972fafc925fd3e31ff0fcc6f72e38ed2fb8248c8896c81f8053",  # 036.jpg
    "ae9c3a8edb9cffda2851dab19aa9cf6a739e4d8de73759c503c86e224724d32f",  # 037.jpg
    "ec083079657fd14972a7dc4f790a98105866ec1bea56e03ce488da5b22dd69c7",  # 037.jpg
    "6b50f8c8347a3812f1544850cbb58add8a89832f7e5d38984ef9c4b9abcd15ec",  # 038.jpg
    "1b4befc3f07a4b2a9a0994e3ad582320f511cea6cd97fa6371d60e559bc147aa",  # 038.jpg
    "716209360e14e560d7a699b20fc995da2834f34b887c42e60abbf7042dd600b2",  # 039.jpg
    "32fa0881fb4470d725a52e7ff10539e3f354e58ce0a0d86ae659031acd9d87f4",  # 039.jpg
    "5a5845a83b0c87a5d55d283cc72404e225ab6fb17a8ccb17e6c67aff3a615c58",  # 040.jpg
    "8ccd6a15c175673267666a4e4ecfb895019860c17069454399073d0fa80b1f3a",  # 040.jpg
    "cadd73e00adf817b1d28a7c13b5e7de380f8694076627274d1e065a75d13f1fe",  # 041.jpg
    "fb21b9a628f07d46bf9b41acfd5f6b6a698c6cdc9a291e536b8ed1e445f19608",  # 041.jpg
    "6ed99c19c816b4185698f53f269ef49962266a3a304da0f76817e49f158ad8e1",  # 042.jpg
    "e110a50408b7b70cddae9f0ed9454f87531c0a032b680e6b195054d946c6485e",  # 042.jpg
    "67c274202baa4be7014cb7c37d320a6c2d36a427df4b4fe0dd6142cc0ac16beb",  # 043.jpg
    "a698fac7e46c1d92e3b48aa29072a759992698552e0dc6934e5ce66ca6555968",  # 043.jpg
    "e979434108eb0ff671b994fce7ea8aeed0b279c3676bf3e55b71cc053856e1b5",  # 044.jpg
    "aaf733beafb5b34163d9f3c73ecc3d11750189426c90492f92bf70761cfef444",  # 044.jpg
    "0e98bb0e05a369af19f3e7da424e0ba71e03e0ade261b891658d0c55f6f8bd7d",  # 045.jpg
    "07ba68dcd66a0e74dc6c2c9658daf08d5a4c9a57e5db2ea4e15ea7783e1c51e1",  # 045.jpg
    "f453159b15fece6328baf7896566a9c70aa0fa6ddacc1bdbbdff6e1d07acab8e",  # 046.jpg
    "b671d9ec6256226f38f1d3e7f23371e609ee237c84c4c8a5cc253395ef1116e8",  # 046.jpg
    "a54365a22e0cac5999afcfb3c1f2ab6cfd431cad7c1d3e1396a8de82677f7e07",  # 047.jpg
    "07dfe29f52b4cabebb03646db348f6a729f80f804eb42b195bd057cb773b971e",  # 047.jpg
    "c00d1cc7eb5c31b9ae2acafb7c0e27960c215c8b5558f6a8057490266f3a0646",  # 048.jpg
    "26b4609a7bc0cbe7f7232174415f9c89c5f43d007a9305139780cb617f77f348",  # 048.jpg
    "3510482b20a5b93eb8e8558227fa80f8460581f71e433932d11bac989e9d17fc",  # 049.jpg
    "85aec922735577f403121f36bd01b2035fbc2cdb5e4e916066cff128b5afde37"   # 049.jpg
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
    if check50.hash("000.jpg") != HASHES[0] and \
       check50.hash("000.jpg") != HASHES[1]:
        raise check50.Failure("recovered image does not match")

@check50.check(compiles)
def middle_images():
    """recovers middle images correctly"""
    check50.run("./recover card.raw").exit(0, timeout=10)
    for i in range(1, int(len(HASHES) / 2) - 1):
        if HASHES[i*2]   != check50.hash("{:03d}.jpg".format(i)) and \
           HASHES[i*2+1] != check50.hash("{:03d}.jpg".format(i)):
            raise check50.Failure("recovered image does not match")

@check50.check(compiles)
def last_image():
    """recovers 049.jpg correctly"""
    check50.run("./recover card.raw").exit(0, timeout=10)
    if check50.hash("049.jpg") != HASHES[-2] and \
       check50.hash("049.jpg") != HASHES[-1]:
        raise check50.Failure("recovered image does not match")
