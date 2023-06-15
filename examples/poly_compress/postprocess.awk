BEGIN             {i = 0;}
/mov ([^ ]*) dl;/ {printf "mov b_%d dl;\n", i; i++;next;}
/.*/              {print $0;}
