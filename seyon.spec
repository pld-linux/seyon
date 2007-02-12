Summary:	A complete full-featured telecommunications package for X11
Summary(pl.UTF-8):	W pełni funkcjonalny pakiet telekomunikacyjny dla X11
Name:		seyon
Version:	2.20c
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	ftp://ibiblio.org/pub/Linux/apps/serialcomm/dialout/%{name}-%{version}.tar.gz
# Source0-md5:	82ab5470a93ef591fe4c3b2b40f91469
Patch0:		%{name}-dec.patch
Patch1:		%{name}-config.patch
Patch2:		%{name}-debian.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
A complete full-featured telecommunications package for the X Window
System.

%description -l pl.UTF-8
W pełni funkcjonalny pakiet telekomunikacyjny dla Systemu X Window.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
chmod u+x makever.sh

%build
/usr/X11R6/bin/xmkmf
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	BINDIR=%{_bindir} \
	HELPFILE="-DHELPFILE=\\\"%{_datadir}/%{name}/seyon.help\\\""

rm -f doc/*.old

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir}

install %{name}.help $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.help
ln -sf /usr/X11R6/bin/xterm $RPM_BUILD_ROOT%{_bindir}/seyon-emu
install %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc 1-* startup
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_appdefsdir}/*
%{_mandir}/man?/*
