# $Revision: 1.4 $Date: 2000-04-01 11:14:54 $
Summary:	Poor man's memory profile
Name:		mpr
Version:	1.9
Release:	1
Copyright:	distributable
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze
Source:		ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/%{name}-%{version}.tar.gz
Requires:	gdb, gcc, binutils
ExclusiveArch:	%ix86
ExclusiveOs:	Linux
Requires:	gawk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mpr can be used to find malloc/realloc memory leaks and memory allocation
statistics and patterns - it does not find memory corruption errors. It uses
a simple, brute force strategy - log all memory alloc/free requests to a
file and then post-process this log file once the program has terminated.

%prep
%setup -q
./configure x86-linux

%build
make CCFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}

install {mpr,mprcc,mprfl,mprhi,mprlk,mprmap,mprsz,mprpc,mprnm,mprdem} \
	$RPM_BUILD_ROOT%{_bindir}
install libmpr.a $RPM_BUILD_ROOT%{_libdir}

strip $RPM_BUILD_ROOT%{_bindir}/mprdem

gzip -9nf README DOC FAQ BUGS LOG LICENSE README.PERL README.SLOW

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_libdir}/*
%attr(755,root,root) %{_bindir}/*
