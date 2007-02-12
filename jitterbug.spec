Summary:	Tool for problem reporting and tracking developed
Summary(pl.UTF-8):   Narzędzie do raportowania i śledzenia rozwoju
Name:		jitterbug
Version:	1.6.2
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.samba.org/pub/jitterbug/%{name}-%{version}.tar.gz
# Source0-md5:	a01f5807ff53c2ebcf1915fa9c472236
URL:		http://samba.anu.edu.au/jitterbug/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JitterBug is a cgi-bin tool for problem reporting and tracking
developed by Andrew Tridgell for the Samba Team.

%description -l pl.UTF-8
JitterBug jest skryptem cgi-bin służącym do reportowania i śledzenia
błędów. JitterBug został stworzony przez Andrew Tridgell dla Zespołu
Samby.

%prep
%setup -q

%build
cd source
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/services/httpd/cgi-bin \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name} \
	$RPM_BUILD_ROOT%{_bindir}

install source/%{name}		$RPM_BUILD_ROOT/home/services/httpd/cgi-bin/%{name}
install source/new_message	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* mail/* config
%attr(4750,root,http) /home/services/httpd/cgi-bin/%{name}
%attr(755, root,root) %{_bindir}/*
%attr(755, root,root) %dir %{_sysconfdir}/%{name}
