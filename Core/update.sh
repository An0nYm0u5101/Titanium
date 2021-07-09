#!/bin/bash
GREEN=$(tput setaf 2)
LIGHTBLUE=$(tput setaf 6)
WHITE=$(tput setaf 15)


function check {
  attempts=5;
  Password=$(sed -nr "/^\[Settings\]/ { :l /^Password[ ]*=/ { s/.*=[ ]*//; p; q;}; n; b l;}" <Configuration/Configuration.ini)
  printf "${LIGHTBLUE}\nINSERT YOUR UPDATE PASSWORD YOU HAVE $attempts ATTEMPTS\n\n"
  while [[ $attempts>0 ]];
    do
      read -p "$GREEN[*TITANIUM*]$WHITE-->" pass
      while [[ $pass == "" ]]
      do
        printf "${LIGHTBLUE}\nINSERT YOUR UPDATE PASSWORD YOU HAVE $attempts ATTEMPTS\n\n"
        read -p "$GREEN[*TITANIUM*]$WHITE-->" pass
      done
      if [ "$pass" == "$Password" ];
        then
        printf "${LIGHTBLUE}\nPASSWORD CORRECT!\n"
        update
      fi
        ((attempts=attempts-1))
        printf "${LIGHTBLUE}\nWRONG PASSWORD REMAINING: $attempts ATTEMPTS\n\n"
    done
    printf "${WHITE}\nYOU HAVE: $attempts PRESS ENTER TO EXIT"
    read -p
    exit 1
}


function update {
  Update_path=$(sed -nr "/^\[Settings\]/ { :l /^Path[ ]*=/ { s/.*=[ ]*//; p; q;}; n; b l;}" <Configuration/Configuration.ini)
  cd $Update_path
  mv Titanium Titanium2  &>/dev/null
  git clone https://github.com/Lucksi/Titanium &>/dev/null | printf "$WHITE\nUPDATING MR.HOLMES..\n"

  if [ $? -eq  0 ];
    then
    cd $Update_path
    cd Titanium
    chmod +x install.sh
    cd ../
    printf "${WHITE}\nWOULD YOU LIKE TO DELETE THE OLD FILES?(1)YES(2)NO\n\n"
    read -p "$GREEN[*TITANIUM*]$WHITE-->" conf
    if [ $conf = 1 ];
      then
      rm -r Titanium2 &>/dev/null | printf "${LIGHTBLUE}\nDELETING OLD TITANIUM FILES"
    else
      printf "${LIGHTBLUE}\nKEEPING OLD MR.HOLMES FILES"
    fi
    sleep 2
    printf "${WHITE}\n\nTITANIUM UPDATED CORRECTLY WOULD YOU LIKE TO RUN THE INSTALLER NOW?(1)YES(2)NO\n\n"
    read -p "$GREEN[*TITANIUM*]$WHITE-->" confvar
    if [ $confvar = 1 ];
      then
        cd Titanium
          ./install.sh
          exit 1
    fi
      printf "${WHITE}\nPRESS ENTER TO EXIT"
      read -p
      exit 1

  fi
    printf "${LIGHTBLUE}\n\nMR.HOLMES NOT INSTALLED HAVE YOU CHECKED YOUR INTERNET CONNECTION?\n\n"
    mv Titanium2 Titanium
    exit 1
}
check
