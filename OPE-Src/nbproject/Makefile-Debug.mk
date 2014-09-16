#
# Generated Makefile - do not edit!
#
# Edit the Makefile in the project folder instead (../Makefile). Each target
# has a -pre and a -post target defined where you can add customized code.
#
# This makefile implements configuration specific macros and targets.


# Environment
MKDIR=mkdir
CP=cp
GREP=grep
NM=nm
CCADMIN=CCadmin
RANLIB=ranlib
CC=gcc
CCC=g++
CXX=g++
FC=gfortran
AS=as

# Macros
CND_PLATFORM=GNU-Linux-x86
CND_DLIB_EXT=so
CND_CONF=Debug
CND_DISTDIR=dist
CND_BUILDDIR=build

# Include project Makefile
include Makefile

# Object Directory
OBJECTDIR=${CND_BUILDDIR}/${CND_CONF}/${CND_PLATFORM}

# Object Files
OBJECTFILES= \
	${OBJECTDIR}/_ext/1376241646/InertiaCalculations.o \
	${OBJECTDIR}/_ext/1376241646/Minimization.o \
	${OBJECTDIR}/_ext/1376241646/OPEMain.o \
	${OBJECTDIR}/_ext/1376241646/OPESettings.o \
	${OBJECTDIR}/_ext/1376241646/OPEUtils.o \
	${OBJECTDIR}/_ext/1376241646/ObjectPoseEstimator.o \
	${OBJECTDIR}/_ext/1376241646/Plane.o \
	${OBJECTDIR}/_ext/1376241646/PointCloudCapture.o \
	${OBJECTDIR}/_ext/1376241646/SQFitting.o


# C Compiler Flags
CFLAGS=

# CC Compiler Flags
CCFLAGS=
CXXFLAGS=

# Fortran Compiler Flags
FFLAGS=

# Assembler Flags
ASFLAGS=

# Link Libraries and Options
LDLIBSOPTIONS=-lboost_system -lboost_thread -lOpenNI -lpcl_common -lpcl_features -lpcl_filters -lpcl_io -lpcl_search -lpcl_segmentation -lpcl_surface -lpcl_visualization -lvtkCommon -lvtkFiltering -lvtkHybrid -lvtkRendering

# Build Targets
.build-conf: ${BUILD_SUBPROJECTS}
	"${MAKE}"  -f nbproject/Makefile-${CND_CONF}.mk bin/${CND_CONF}/${CND_PLATFORM}/ope-new

bin/${CND_CONF}/${CND_PLATFORM}/ope-new: ${OBJECTFILES}
	${MKDIR} -p bin/${CND_CONF}/${CND_PLATFORM}
	${LINK.cc} -o bin/${CND_CONF}/${CND_PLATFORM}/ope-new ${OBJECTFILES} ${LDLIBSOPTIONS}

${OBJECTDIR}/_ext/1376241646/InertiaCalculations.o: /home/neroxtu/Desktop/MYAH/OPE-New/src/InertiaCalculations.cpp 
	${MKDIR} -p ${OBJECTDIR}/_ext/1376241646
	${RM} "$@.d"
	$(COMPILE.cc) -g -Iinclude -I/usr/include/pcl-1.7 -I/usr/include/eigen3 -I/usr/include/vtk-5.8 -I/usr/include/ni -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/_ext/1376241646/InertiaCalculations.o /home/neroxtu/Desktop/MYAH/OPE-New/src/InertiaCalculations.cpp

${OBJECTDIR}/_ext/1376241646/Minimization.o: /home/neroxtu/Desktop/MYAH/OPE-New/src/Minimization.cpp 
	${MKDIR} -p ${OBJECTDIR}/_ext/1376241646
	${RM} "$@.d"
	$(COMPILE.cc) -g -Iinclude -I/usr/include/pcl-1.7 -I/usr/include/eigen3 -I/usr/include/vtk-5.8 -I/usr/include/ni -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/_ext/1376241646/Minimization.o /home/neroxtu/Desktop/MYAH/OPE-New/src/Minimization.cpp

${OBJECTDIR}/_ext/1376241646/OPEMain.o: /home/neroxtu/Desktop/MYAH/OPE-New/src/OPEMain.cpp 
	${MKDIR} -p ${OBJECTDIR}/_ext/1376241646
	${RM} "$@.d"
	$(COMPILE.cc) -g -Iinclude -I/usr/include/pcl-1.7 -I/usr/include/eigen3 -I/usr/include/vtk-5.8 -I/usr/include/ni -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/_ext/1376241646/OPEMain.o /home/neroxtu/Desktop/MYAH/OPE-New/src/OPEMain.cpp

${OBJECTDIR}/_ext/1376241646/OPESettings.o: /home/neroxtu/Desktop/MYAH/OPE-New/src/OPESettings.cpp 
	${MKDIR} -p ${OBJECTDIR}/_ext/1376241646
	${RM} "$@.d"
	$(COMPILE.cc) -g -Iinclude -I/usr/include/pcl-1.7 -I/usr/include/eigen3 -I/usr/include/vtk-5.8 -I/usr/include/ni -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/_ext/1376241646/OPESettings.o /home/neroxtu/Desktop/MYAH/OPE-New/src/OPESettings.cpp

${OBJECTDIR}/_ext/1376241646/OPEUtils.o: /home/neroxtu/Desktop/MYAH/OPE-New/src/OPEUtils.cpp 
	${MKDIR} -p ${OBJECTDIR}/_ext/1376241646
	${RM} "$@.d"
	$(COMPILE.cc) -g -Iinclude -I/usr/include/pcl-1.7 -I/usr/include/eigen3 -I/usr/include/vtk-5.8 -I/usr/include/ni -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/_ext/1376241646/OPEUtils.o /home/neroxtu/Desktop/MYAH/OPE-New/src/OPEUtils.cpp

${OBJECTDIR}/_ext/1376241646/ObjectPoseEstimator.o: /home/neroxtu/Desktop/MYAH/OPE-New/src/ObjectPoseEstimator.cpp 
	${MKDIR} -p ${OBJECTDIR}/_ext/1376241646
	${RM} "$@.d"
	$(COMPILE.cc) -g -Iinclude -I/usr/include/pcl-1.7 -I/usr/include/eigen3 -I/usr/include/vtk-5.8 -I/usr/include/ni -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/_ext/1376241646/ObjectPoseEstimator.o /home/neroxtu/Desktop/MYAH/OPE-New/src/ObjectPoseEstimator.cpp

${OBJECTDIR}/_ext/1376241646/Plane.o: /home/neroxtu/Desktop/MYAH/OPE-New/src/Plane.cpp 
	${MKDIR} -p ${OBJECTDIR}/_ext/1376241646
	${RM} "$@.d"
	$(COMPILE.cc) -g -Iinclude -I/usr/include/pcl-1.7 -I/usr/include/eigen3 -I/usr/include/vtk-5.8 -I/usr/include/ni -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/_ext/1376241646/Plane.o /home/neroxtu/Desktop/MYAH/OPE-New/src/Plane.cpp

${OBJECTDIR}/_ext/1376241646/PointCloudCapture.o: /home/neroxtu/Desktop/MYAH/OPE-New/src/PointCloudCapture.cpp 
	${MKDIR} -p ${OBJECTDIR}/_ext/1376241646
	${RM} "$@.d"
	$(COMPILE.cc) -g -Iinclude -I/usr/include/pcl-1.7 -I/usr/include/eigen3 -I/usr/include/vtk-5.8 -I/usr/include/ni -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/_ext/1376241646/PointCloudCapture.o /home/neroxtu/Desktop/MYAH/OPE-New/src/PointCloudCapture.cpp

${OBJECTDIR}/_ext/1376241646/SQFitting.o: /home/neroxtu/Desktop/MYAH/OPE-New/src/SQFitting.cpp 
	${MKDIR} -p ${OBJECTDIR}/_ext/1376241646
	${RM} "$@.d"
	$(COMPILE.cc) -g -Iinclude -I/usr/include/pcl-1.7 -I/usr/include/eigen3 -I/usr/include/vtk-5.8 -I/usr/include/ni -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/_ext/1376241646/SQFitting.o /home/neroxtu/Desktop/MYAH/OPE-New/src/SQFitting.cpp

# Subprojects
.build-subprojects:

# Clean Targets
.clean-conf: ${CLEAN_SUBPROJECTS}
	${RM} -r ${CND_BUILDDIR}/${CND_CONF}
	${RM} bin/${CND_CONF}/${CND_PLATFORM}/ope-new

# Subprojects
.clean-subprojects:

# Enable dependency checking
.dep.inc: .depcheck-impl

include .dep.inc
