# $Revision: 1.20 $Date: 2007-02-13 07:16:48 $
Summary:	Poor man's memory profile
Summary(pl.UTF-8):	Profiler pamięci dla ubogich
Name:		mpr
Version:	2.8
Release:	1
License:	distributable
Group:		Development/Debuggers
Source0:	ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/%{name}-%{version}.tar.gz
# Source0-md5:	ef03beef7200516a37184d0be7e0e9f7
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

%description -l pl.UTF-8
mpr może być używany do szukania wycieków pamięci przy malloc/realloc
oraz określania statystyk alokacji pamięci - nie szuka błędów
naruszenia pamięci. Używa prostej strategii brute-force - loguje
wszystkie zlecenia alokacji/zwolnienia do pliku, a po zakończeniu
programu przeprowadza postprocessing tego pliku.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html BUGS FAQ LOG README
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*.a
