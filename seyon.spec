Summary:	A complete full-featured telecommunications package for X11
Name:		seyon
Version:	2.20c
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	ftp://ibiblio.org/pub/Linux/apps/serialcomm/dialout/%{name}-%{version}.tar.gz
# Source0-md5:	82ab5470a93ef591fe4c3b2b40f91469
Patch0:		%{name}-dec.patch
Patch1:		%{name}-config.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A complete full-featured telecommunications package for the X Window System.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
chmod u+x makever.sh

%build
/usr/X11R6/bin/xmkmf
%{__make} \
	BINDIR=%{_bindir} \
	HELPFILE="-DHELPFILE=\\\"%{_datadir}/%{name}/seyon.help\\\""

rm -f doc/*.old

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_mandir}/man1}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	BINDIR=%{_bindir}

install %{name}.help $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.help
ln -s %{_prefix}/X11R6/bin/xterm $RPM_BUILD_ROOT%{_bindir}/seyon-emu
install %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc 1-*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_prefix}/X11R6/lib/X11/app-defaults/*
%{_mandir}/man?/*
