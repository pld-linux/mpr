# $Revision: 1.9 $Date: 2002-01-18 02:13:58 $
Summary:	Poor man's memory profile
Summary(pl):	Profiler pami�ci dla ubogich
Name:		mpr
Version:	1.9
Release:	1
License:	distributable
Group:		Development/Debuggers
Group(de):	Entwicklung/Debugger
Group(pl):	Programowanie/Odpluskwiacze
Source0:	ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/%{name}-%{version}.tar.gz
Requires:	gdb, gcc, binutils
ExclusiveArch:	%{ix86}
ExclusiveOs:	Linux
Requires:	gawk
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

gzip -9nf README DOC FAQ BUGS LOG LICENSE README.PERL README.SLOW

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_libdir}/*
%attr(755,root,root) %{_bindir}/*
