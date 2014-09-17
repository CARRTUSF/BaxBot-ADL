#!/bin/sh

# ANSI Color -- use these variables to easily have different color
#    and format output. Make sure to output the reset sequence after 
#    colors (f = foreground, b = background), and use the 'off'
#    feature for anything you turn on.

initializeANSI()
{
  blackf='\033[30m';   redf='\033[31m';    greenf='\033[32m'
  yellowf='\033[33m';  bluef='\033[34m';   purplef='\033[35m'
  cyanf='\033[36m';    whitef='\033[37m'
 
  boldon='\033[1m';    reset='\033[0m'
}

# note in this first use that switching colors doesn't require a reset
# first - the new color overrides the old one.

initializeANSI
clear
while [ 1 ]
do
echo "$(cat << EOF)"
   ${boldon}${redf}▀▄   ▄▀  ${reset}    ${boldon}${greenf}▄▄▄████▄▄▄ ${reset}   ${boldon}${yellowf}  ▄██▄  ${reset}     ${boldon}${bluef}▀▄   ▄▀  ${reset}    ${boldon}${purplef}▄▄▄████▄▄▄ ${reset}   ${boldon}${cyanf}  ▄██▄  ${reset}
  ${boldon}${redf}▄█▀███▀█▄ ${reset}   ${boldon}${greenf}███▀▀██▀▀███${reset}   ${boldon}${yellowf}▄█▀██▀█▄${reset}    ${boldon}${bluef}▄█▀███▀█▄ ${reset}   ${boldon}${purplef}███▀▀██▀▀███${reset}   ${boldon}${cyanf}▄█▀██▀█▄${reset}
 ${boldon}${redf}█▀███████▀█${reset}   ${boldon}${greenf}▀▀▀██▀▀██▀▀▀${reset}   ${boldon}${yellowf}▀▀█▀▀█▀▀${reset}   ${boldon}${bluef}█▀███████▀█${reset}   ${boldon}${purplef}▀▀▀██▀▀██▀▀▀${reset}   ${boldon}${cyanf}▀▀█▀▀█▀▀${reset}
 ${boldon}${redf}▀ ▀▄▄ ▄▄▀ ▀${reset}   ${boldon}${greenf}▄▄▀▀ ▀▀ ▀▀▄▄${reset}   ${boldon}${yellowf}▄▀▄▀▀▄▀▄${reset}   ${boldon}${bluef}▀ ▀▄▄ ▄▄▀ ▀${reset}   ${boldon}${purplef}▄▄▀▀ ▀▀ ▀▀▄▄${reset}   ${boldon}${cyanf}▄▀▄▀▀▄▀▄${reset}

   ${boldon}${redf}▀▄   ▄▀  ${reset}    ${boldon}${greenf}▄▄▄████▄▄▄ ${reset}   ${boldon}${yellowf}  ▄██▄  ${reset}     ${boldon}${bluef}▀▄   ▄▀  ${reset}    ${boldon}${purplef}▄▄▄████▄▄▄ ${reset}   ${boldon}${cyanf}  ▄██▄  ${reset}
  ${boldon}${redf}▄█▀███▀█▄ ${reset}                                                          ${boldon}${cyanf}▄█▀██▀█▄${reset}
 ${boldon}${redf}█▀███████▀█${reset}      ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .       ▌ ▐·▄▄▄ .▄▄▄        ${boldon}${cyanf}▀▀█▀▀█▀▀${reset}
 ${boldon}${redf}▀ ▀▄▄ ▄▄▀ ▀${reset}     ▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·▪     ▪█·█▌▀▄.▀·▀▄ █·      ${boldon}${cyanf}▄▀▄▀▀▄▀▄${reset}
                 ▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄ ▄█▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄    
   ${boldon}${redf}▀▄   ▄▀  ${reset}     ▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌▐█▌.▐▌ ███ ▐█▄▄▌▐█•█▌      ${boldon}${cyanf}  ▄██▄  ${reset}
  ${boldon}${redf}▄█▀███▀█▄ ${reset}      ▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀  ▀█▄▀▪. ▀   ▀▀▀ .▀  ▀      ${boldon}${cyanf}▄█▀██▀█▄${reset}
 ${boldon}${redf}█▀███████▀█${reset}                                                          ${boldon}${cyanf}▀▀█▀▀█▀▀${reset}
 ${boldon}${redf}▀ ▀▄▄ ▄▄▀ ▀${reset}   ${boldon}${greenf}▄▄▀▀ ▀▀ ▀▀▄▄${reset}   ${boldon}${yellowf}▄▀▄▀▀▄▀▄${reset}   ${boldon}${bluef}▀ ▀▄▄ ▄▄▀ ▀${reset}   ${boldon}${purplef}▄▄▀▀ ▀▀ ▀▀▄▄${reset}   ${boldon}${cyanf}▄▀▄▀▀▄▀▄${reset}

   ${boldon}${redf}▀▄   ▄▀  ${reset}    ${boldon}${greenf}▄▄▄████▄▄▄ ${reset}   ${boldon}${yellowf}  ▄██▄  ${reset}     ${boldon}${bluef}▀▄   ▄▀  ${reset}    ${boldon}${purplef}▄▄▄████▄▄▄ ${reset}   ${boldon}${cyanf}  ▄██▄  ${reset}
  ${boldon}${redf}▄█▀███▀█▄ ${reset}   ${boldon}${greenf}███▀▀██▀▀███${reset}   ${boldon}${yellowf}▄█▀██▀█▄${reset}    ${boldon}${bluef}▄█▀███▀█▄ ${reset}   ${boldon}${purplef}███▀▀██▀▀███${reset}   ${boldon}${cyanf}▄█▀██▀█▄${reset}
 ${boldon}${redf}█▀███████▀█${reset}   ${boldon}${greenf}▀▀▀██▀▀██▀▀▀${reset}   ${boldon}${yellowf}▀▀█▀▀█▀▀${reset}   ${boldon}${bluef}█▀███████▀█${reset}   ${boldon}${purplef}▀▀▀██▀▀██▀▀▀${reset}   ${boldon}${cyanf}▀▀█▀▀█▀▀${reset}
 ${boldon}${redf}▀ ▀▄▄ ▄▄▀ ▀${reset}   ${boldon}${greenf}▄▄▀▀ ▀▀ ▀▀▄▄${reset}   ${boldon}${yellowf}▄▀▄▀▀▄▀▄${reset}   ${boldon}${bluef}▀ ▀▄▄ ▄▄▀ ▀${reset}   ${boldon}${purplef}▄▄▀▀ ▀▀ ▀▀▄▄${reset}   ${boldon}${cyanf}▄▀▄▀▀▄▀▄${reset}

    $1
EOF
sleep 0.5s
clear
echo "$(cat << EOF)"
   ${boldon}${redf}▀▄   ▄▀  ${reset}    ${boldon}${greenf}▄▄▄████▄▄▄ ${reset}   ${boldon}${yellowf}  ▄██▄  ${reset}     ${boldon}${bluef}▀▄   ▄▀  ${reset}    ${boldon}${purplef}▄▄▄████▄▄▄ ${reset}   ${boldon}${cyanf}  ▄██▄  ${reset}
  ${boldon}${redf}▄█▀███▀█▄ ${reset}   ${boldon}${greenf}███▀▀██▀▀███${reset}   ${boldon}${yellowf}▄█▀██▀█▄${reset}    ${boldon}${bluef}▄█▀███▀█▄ ${reset}   ${boldon}${purplef}███▀▀██▀▀███${reset}   ${boldon}${cyanf}▄█▀██▀█▄${reset}
 ${boldon}${redf}█▀███████▀█${reset}   ${boldon}${greenf}▀▀▀██▀▀██▀▀▀${reset}   ${boldon}${yellowf}▀▀█▀▀█▀▀${reset}   ${boldon}${bluef}█▀███████▀█${reset}   ${boldon}${purplef}▀▀▀██▀▀██▀▀▀${reset}   ${boldon}${cyanf}▀▀█▀▀█▀▀${reset}
 ${boldon}${redf}▀ ▀▄▄ ▄▄▀ ▀${reset}   ${boldon}${greenf}▄▄▀▀ ▀▀ ▀▀▄▄${reset}   ${boldon}${yellowf}▄▀▄▀▀▄▀▄${reset}   ${boldon}${bluef}▀ ▀▄▄ ▄▄▀ ▀${reset}   ${boldon}${purplef}▄▄▀▀ ▀▀ ▀▀▄▄${reset}   ${boldon}${cyanf}▄▀▄▀▀▄▀▄${reset}

   ${boldon}${redf}▀▄   ▄▀  ${reset}    ${boldon}${greenf}▄▄▄████▄▄▄ ${reset}   ${boldon}${yellowf}  ▄██▄  ${reset}     ${boldon}${bluef}▀▄   ▄▀  ${reset}    ${boldon}${purplef}▄▄▄████▄▄▄ ${reset}   ${boldon}${cyanf}  ▄██▄  ${reset}
  ${boldon}${redf}▄█▀███▀█▄ ${reset}   ${boldon}${greenf}███▀▀██▀▀███${reset}   ${boldon}${yellowf}▄█▀██▀█▄${reset}    ${boldon}${bluef}▄█▀███▀█▄ ${reset}   ${boldon}${purplef}███▀▀██▀▀███${reset}   ${boldon}${cyanf}▄█▀██▀█▄${reset}
 ${boldon}${redf}█▀███████▀█${reset}   ${boldon}${greenf}▀▀▀██▀▀██▀▀▀${reset}   ${boldon}${yellowf}▀▀█▀▀█▀▀${reset}   ${boldon}${bluef}█▀███████▀█${reset}   ${boldon}${purplef}▀▀▀██▀▀██▀▀▀${reset}   ${boldon}${cyanf}▀▀█▀▀█▀▀${reset}
 ${boldon}${redf}▀ ▀▄▄ ▄▄▀ ▀${reset}   ${boldon}${greenf}▄▄▀▀ ▀▀ ▀▀▄▄${reset}   ${boldon}${yellowf}▄▀▄▀▀▄▀▄${reset}   ${boldon}${bluef}▀ ▀▄▄ ▄▄▀ ▀${reset}   ${boldon}${purplef}▄▄▀▀ ▀▀ ▀▀▄▄${reset}   ${boldon}${cyanf}▄▀▄▀▀▄▀▄${reset}

   ${boldon}${redf}▀▄   ▄▀  ${reset}    ${boldon}${greenf}▄▄▄████▄▄▄ ${reset}   ${boldon}${yellowf}  ▄██▄  ${reset}     ${boldon}${bluef}▀▄   ▄▀  ${reset}    ${boldon}${purplef}▄▄▄████▄▄▄ ${reset}   ${boldon}${cyanf}  ▄██▄  ${reset}
  ${boldon}${redf}▄█▀███▀█▄ ${reset}   ${boldon}${greenf}███▀▀██▀▀███${reset}   ${boldon}${yellowf}▄█▀██▀█▄${reset}    ${boldon}${bluef}▄█▀███▀█▄ ${reset}   ${boldon}${purplef}███▀▀██▀▀███${reset}   ${boldon}${cyanf}▄█▀██▀█▄${reset}
 ${boldon}${redf}█▀███████▀█${reset}   ${boldon}${greenf}▀▀▀██▀▀██▀▀▀${reset}   ${boldon}${yellowf}▀▀█▀▀█▀▀${reset}   ${boldon}${bluef}█▀███████▀█${reset}   ${boldon}${purplef}▀▀▀██▀▀██▀▀▀${reset}   ${boldon}${cyanf}▀▀█▀▀█▀▀${reset}
 ${boldon}${redf}▀ ▀▄▄ ▄▄▀ ▀${reset}   ${boldon}${greenf}▄▄▀▀ ▀▀ ▀▀▄▄${reset}   ${boldon}${yellowf}▄▀▄▀▀▄▀▄${reset}   ${boldon}${bluef}▀ ▀▄▄ ▄▄▀ ▀${reset}   ${boldon}${purplef}▄▄▀▀ ▀▀ ▀▀▄▄${reset}   ${boldon}${cyanf}▄▀▄▀▀▄▀▄${reset}

   ${boldon}${redf}▀▄   ▄▀  ${reset}    ${boldon}${greenf}▄▄▄████▄▄▄ ${reset}   ${boldon}${yellowf}  ▄██▄  ${reset}     ${boldon}${bluef}▀▄   ▄▀  ${reset}    ${boldon}${purplef}▄▄▄████▄▄▄ ${reset}   ${boldon}${cyanf}  ▄██▄  ${reset}
  ${boldon}${redf}▄█▀███▀█▄ ${reset}   ${boldon}${greenf}███▀▀██▀▀███${reset}   ${boldon}${yellowf}▄█▀██▀█▄${reset}    ${boldon}${bluef}▄█▀███▀█▄ ${reset}   ${boldon}${purplef}███▀▀██▀▀███${reset}   ${boldon}${cyanf}▄█▀██▀█▄${reset}
 ${boldon}${redf}█▀███████▀█${reset}   ${boldon}${greenf}▀▀▀██▀▀██▀▀▀${reset}   ${boldon}${yellowf}▀▀█▀▀█▀▀${reset}   ${boldon}${bluef}█▀███████▀█${reset}   ${boldon}${purplef}▀▀▀██▀▀██▀▀▀${reset}   ${boldon}${cyanf}▀▀█▀▀█▀▀${reset}
 ${boldon}${redf}▀ ▀▄▄ ▄▄▀ ▀${reset}   ${boldon}${greenf}▄▄▀▀ ▀▀ ▀▀▄▄${reset}   ${boldon}${yellowf}▄▀▄▀▀▄▀▄${reset}   ${boldon}${bluef}▀ ▀▄▄ ▄▄▀ ▀${reset}   ${boldon}${purplef}▄▄▀▀ ▀▀ ▀▀▄▄${reset}   ${boldon}${cyanf}▄▀▄▀▀▄▀▄${reset}

    $1
EOF
sleep 0.5s
clear
done
