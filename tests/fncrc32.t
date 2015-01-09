The --help flag should give some hints on how to use the command.

  $ fncrc32 --help
  Usage: fncrc32 [OPTIONS] [FILES]...
  
  Options:
    --chunk-size INTEGER
    --help                Show this message and exit.

Running the command on a group of files should give hash results for each.

  $ cd $TESTDIR && fncrc32 "fixtures/joke [391fc5ae].txt" "fixtures/riddle [2a2a2a2a].txt"
    [ 391fc5ae ] "fixtures/joke [391fc5ae].txt"
  ! [ bf3d6242 ] "fixtures/riddle [2a2a2a2a].txt"
