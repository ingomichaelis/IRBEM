!***************************************************************************************************
! Copyright 2004 S. Bourdarie
!
! This file is part of IRBEM-LIB.
!
!    IRBEM-LIB is free software: you can redistribute it and/or modify
!    it under the terms of the GNU Lesser General Public License as published by
!    the Free Software Foundation, either version 3 of the License, or
!    (at your option) any later version.
!
!    IRBEM-LIB is distributed in the hope that it will be useful,
!    but WITHOUT ANY WARRANTY; without even the implied warranty of
!    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
!    GNU Lesser General Public License for more details.
!
!    You should have received a copy of the GNU Lesser General Public License
!    along with IRBEM-LIB.  If not, see <http://www.gnu.org/licenses/>.
!
	REAL*8     baddata
	INTEGER*4  Nalp,Nreb_def,Nder_def,Ntet_def
	PARAMETER  (baddata=-1.d31)
!	PARAMETER (Nreb_def = 50, Nder_def = 25, Ntet_def = 720)
	PARAMETER (Nreb_def = 50, Nder_def = 25, Ntet_def = 1440)
	PARAMETER (Nalp=25)
