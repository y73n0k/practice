from sage.all import *
from Crypto.Util.number import long_to_bytes as ltb


n = 13914094471031206586811099404378427923436563978304923491145550714629202780726806053965344191687059365342053515509083584729011804256999731344976793761607552187275878077972381494638859048924167985590157197372887535988137115904055078624736906939563172487287289071854500796216938592689853984981203162966605237613640061142661892657548133357294387664465092116973984179583244163509612412300093511455169906315419559490292851670109647111737632234867307510873905832996706390273120900188944333097414218346042135912258576842976376029913563225422702460509894089257269994460063079592056677602183483610219727023433920194675710632297
e = 265729
c = 351680421488240023203692966101751256410186061412521124260468655315150209875597174488144250495293510417817454153870657741319397611987113859914783725822275931701135190489289630106163826521801193362540524367507263561361707670539957820126282343911188930529209132769656194733155331246073843795953279457489127254900379603959826727765969892966835263616481231178038740
print("ictf{" + ltb(round(pow(c // 3, 1 / 5))).decode() + "}")
