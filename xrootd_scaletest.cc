#include <iostream>
#include <fstream>
#include <sys/time.h>

#include "XrdClient/XrdClient.hh"

int main(int argc, char** argv) {

  if (argc == 2) {
    std::cout<<"one argument, and it is...\n"<<argv[1]<<std::endl;
  }
  else {
    std::cout<<"Usage: ./xrd_test list_of_input_files \n"<<std::endl;
  }

  std::ifstream input_files(argv[1]);
  std::string line;

  if ( input_files.is_open() ) {
    while ( getline ( input_files, line) ) {
      std::cout<<"line : "<<line<<std::endl;
      XrdClient *cli = new XrdClient( line.c_str() );

      // file opening timestamp
      timeval tim;
      gettimeofday(&tim, NULL);
      double t1=tim.tv_sec+(tim.tv_usec/1000000.0);
    
      //cli->Open( 0, 0);
      //if (!cli->IsOpen() ) {
      if ( !cli->Open(0, 0) ||
             (cli->LastServerResp()->status != kXR_ok ) ) {
        // client failed to open file properly
        printf("failed to open file %s \n", line.c_str());
      }
      cli->Close();

      // file closing timestamp
      gettimeofday(&tim, NULL);
      double t2=tim.tv_sec+(tim.tv_usec/1000000.0);
      printf("%.6lf seconds elapsed\n", t2-t1);
    
    }
  }

  return 0;
}
