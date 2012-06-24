# $Revision: 1.14 $Date: 2003-09-09 11:05:25 $
Summary:	Poor man's memory profile
Summary(pl):	Profiler pami�ci dla ubogich
Name:		mpr
Version:	1.9
Release:	1
License:	distributable
Group:		Development/Debuggers
Source0:	ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/%{name}-%{version}.tar.gz
# Source0-md5:	40c6932c3806eace84fff2a53740ca54
Requires:	gawk
Requires:	gdb
ExclusiveArch:	%{ix86}
ExclusiveOs:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mpr can be used to find malloc/realloc memory leaks and memory
allocation statistics and patterns - it does not find memory
corruption errors. It uses a simple, brute force strategy - log all
memory alloc/free requests to a file and then post-process this log
file once the program has terminated.

%description -l pl
mpr mo�e by� u�ywany do szukania wyciek�w pami�ci przy malloc/realloc
oraz okre�lania statystych alokacji pami�ci - nie szuka b��d�w
naruszenia pami�ci. U�ywa prostej strategii brute-force - loguje
wszystkie zlecenia alokacji/zwolnienia do pliku, a po zako�czeniu
programu przeprowadza postprocessing tego pliku.

%prep
%setup -q
./configure x86-linux

%build
%{__make} CCFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}

install {mpr,mprcc,mprfl,mprhi,mprlk,mprmap,mprsz,mprpc,mprnm,mprdem} \
	$RPM_BUILD_ROOT%{_bindir}
install libmpr.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README DOC FAQ BUGS LOG LICENSE README.PERL README.SLOW
%{_libdir}/*
%attr(755,root,root) %{_bindir}/*
