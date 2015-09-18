CXX=g++
CC=gcc
CFLAGS=-O2 -Wall -Wno-deprecated-declarations
LDFLAGS=-Llib 
INS=-I$(ROOTSYS)include 
CXXX=`root-config --cxx`
CFLAGS += `$(ROOTSYS)bin/root-config --cflags`
#CFLAGS += `root-config --ldflags`
LIBS   = `root-config --glibs`

#OBJS=analysis.o init.o root.o utils.o postInitialResultsAnalysis.o
OBJS=FuncCB.o fitEfficiency.o combine 

.PHONY: clean all test

all: $(OBJS) 

FuncCB.o: 
	$(CXX)  -I ${ROOTSYS}include  -c -o  FuncCB.o   FuncCB.cxx  `${ROOTSYS}bin/root-config --cflags`   `${ROOTSYS}bin/root-config --glibs` -L ${ROOTSYS}/lib -lRooFit 
#	$(CXX) $(INS)   -c -o  init.o  init.cc   $(CFLAGS)  `root-config --glibs` 
fitEfficiency.o: 
	$(CXX)  -I $(ROOTSYS)include -c  -o fitEfficiency.o  fitEfficiency.C  `$(ROOTSYS)bin/root-config --cflags`   `$(ROOTSYS)bin/root-config --glibs` -L ${ROOTSYS}/lib -lRooFit # $(LIBS)
#	$(CXX)  $(INS)  -c  -o root.o root.cc $(CFLAGS)  `root-config --glibs`  # $(LIBS)

#	$(CXX)  $(INS)  -c -o  main.o  main.cpp  $(CFLAGS)  `root-config --glibs`    #$(LIBS)  
combine: 
	$(CXX)  -I $(ROOTSYS)include   -o  combine fitEfficiency.o FuncCB.o  `$(ROOTSYS)bin/root-config --cflags`    `$(ROOTSYS)bin/root-config --glibs`      -lm
#	$(CXX)   $(INS)  -o combine  main.o $(OBJS)   -lm  $(CFLAGS)   `root-config --glibs`      -lm

#test: 
#	./combine

#clean:
#	@rm -f *.o *.exe core* main

##################### Rules #####################
#.cc.o:
#	$(CXX) $(CFLAGS) $(INS) -c $<

#.cpp.o:
#	$(CXX) $(CFLAGS) $(INS) -c $<
